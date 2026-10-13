"""Generate analytics charts + data export."""
from helpers import put

def generate_charts(report, root, A):
    names = [i["model"] for i in report]
    # Dashboard chart view
    chart_view = '''

@login_required_page
def analytics(request):
    from django.db.models import Count
    data = []
'''
    for n in names[:10]:
        chart_view += f"    data.append({{'name': '{n}', 'count': {n}.objects.count()}})\n"
    chart_view += '''    return render(request, 'portal/analytics.html', {'title': 'Analytics', 'data': data, 'stats': get_sidebar_stats()})

@login_required_page
def export_data(request, model_name):
    import csv
    from django.http import HttpResponse
    model = _get_model(request, model_name)
    if isinstance(model, dict): return model
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{model_name}.csv"'
    writer = csv.writer(response)
    fields = [f.name for f in model._meta.fields]
    writer.writerow(fields)
    for obj in model.objects.all().values_list(*fields):
        writer.writerow(obj)
    return response
'''
    put(root, f"{A}/charts_views.py", chart_view)
    # Analytics template
    tpl = '''{% extends "portal/base.html" %}{% block content %}
<div class="heading"><div><p class="eyebrow">ANALYTICS</p><h1>Charts & Reports</h1></div></div>
<div class="stats">{% for d in data %}<div class="card"><span>{{ d.name }}</span><strong>{{ d.count }}</strong><div style="height:{{ d.count }}px;max-height:100px;background:var(--clr);opacity:.3;border-radius:.5rem;margin-top:.5rem"></div></div>{% endfor %}</div>
<section class="panel"><h2>Export</h2><div class="quick-actions">{% for d in data %}<a class="button secondary" href="/export/{{ d.name|lower }}/">Export {{ d.name }}</a>{% endfor %}</div></section>
{% endblock %}'''
    put(root, f"{A}/templates/{A}/analytics.html", tpl)
    print(f"  Charts: analytics page + CSV export for {len(names)} models")
