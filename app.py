#!/usr/bin/env python3
"""Generate Django + DRF portal from Excel."""
import argparse, sys
from pathlib import Path
from helpers import put
from analyser import analyse
from gen_models import generate_models, generate_admin, generate_forms
from gen_api import generate_serializers, generate_api
from gen_views import generate_views, generate_urls
from gen_templates import generate_all as gen_tpl
from gen_css import generate_all as gen_css
from gen_permissions import generate_permissions
from gen_docker import generate_docker
from gen_charts import generate_charts
from gen_pwa import generate_pwa
from gen_tests import generate_tests
from gen_pages import generate_pages
from gen_project import generate_settings, generate_commands, generate_docs

def generate(report, output, title):
    root = Path(output).resolve()
    if root.exists() and any(root.iterdir()):
        raise FileExistsError(f"Not empty: {root}")
    P, A = "portalproj", "portal"
    for d in (P, A, f"{A}/migrations", f"{A}/management", f"{A}/management/commands",
              f"{A}/templates/{A}", f"{A}/static/{A}", f"{A}/templatetags"):
        (root / d).mkdir(parents=True, exist_ok=True)
    for n in (f"{P}/__init__.py", f"{A}/__init__.py", f"{A}/migrations/__init__.py",
              f"{A}/management/__init__.py", f"{A}/management/commands/__init__.py",
              f"{A}/templatetags/__init__.py"):
        put(root, n, "")
    generate_permissions(report, root, A)
    generate_models(report, root, A)
    generate_admin(report, root, A)
    generate_forms(report, root, A)
    generate_serializers(report, root, A)
    generate_api(report, root, A, title)
    generate_views(report, root, A)
    generate_urls(root, A)
    gen_tpl(root, A, title)
    gen_css(report, root, A, title)
    generate_settings(root, P, A)
    generate_commands(report, root, A)
    generate_pages(report, root, A, title)
    generate_docker(report, root, A, title)
    generate_tests(report, root, A)
    generate_charts(report, root, A)
    generate_pwa(report, root, A, title)
    generate_docs(report, root, title)
    print(f"\nDone! Generated: {root}")
    print(f"Models: {', '.join(i['model'] for i in report)}")
    print(f"\nNext: cd {root} && pip install -r requirements.txt && python manage.py makemigrations portal && python manage.py migrate && python manage.py createsuperuser && python manage.py runserver 0.0.0.0:8000")

def main():
    p = argparse.ArgumentParser(description="Excel to Django")
    p.add_argument("--input", required=True)
    p.add_argument("--output", default="generated_app")
    p.add_argument("--project-name", default="MyPortal")
    a = p.parse_args()
    try:
        report = analyse(a.input)
        print(f"Found {len(report)} worksheet(s):")
        for i in report:
            print(f"  {i['sheet']} -> {i['model']} ({len(i['fields'])} fields)")
        generate(report, a.output, a.project_name)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr); sys.exit(1)

if __name__ == "__main__":
    main()
