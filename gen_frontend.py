"""Generate Vue.js frontend from frontend_tpl/."""
from pathlib import Path
from helpers import put
from gen_pages import detect, THEMES

def generate_frontend(report, root, A, T):
    dom = detect(report, T)
    th = THEMES.get(dom, THEMES["general"])
    src = Path(__file__).parent / "frontend_tpl"
    html = ""
    for f in sorted(src.glob("*.html")):
        html += f.read_text(encoding="utf-8")
    js = ""
    for f in sorted(src.glob("*.js")):
        js += f.read_text(encoding="utf-8")
    models = "[" + ",".join('{"name":"%s","sheet":"%s","rows":%d}' % (i["model"], i["sheet"], i["rows"]) for i in report) + "]"
    for part in [html, js]:
        pass
    for key, val in {"__T__":T,"__TITLE__":T,"__TAG__":th["tag"],"__SUB__":th["sub"],
        "__C1__":th["c1"],"__C2__":th["c2"],"__C3__":th["c3"],
        "__R1__":th["r1"],"__R2__":th["r2"],"__R3__":th["r3"],
        "__I1__":th["i1"],"__I2__":th["i2"],"__I3__":th["i3"],
        "__CLR__":"#b9f477","__DOMAIN__":dom,"__API__":"http://localhost:8000",
        "__MODELS__":models,"__COUNT__":str(len(report))}.items():
        html = html.replace(key, val)
        js = js.replace(key, val)
    html = html.replace('<script src="app.js"></script>', "<script>" + js + "</script>")
    put(root, f"{A}/static/{A}/frontend.html", html)
    print(f"  Frontend SPA: {dom} | roles={th['r1']}/{th['r2']}/{th['r3']}")
