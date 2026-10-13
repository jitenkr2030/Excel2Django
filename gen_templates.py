"""Generate HTML templates from tpl_src/."""
from pathlib import Path
from helpers import put

def generate_all(root, A, T):
    src = Path(__file__).parent / "tpl_src"
    dst = f"{A}/templates/{A}"
    for f in sorted(src.glob("*.html")):
        html = f.read_text(encoding="utf-8").replace("__T__", T)
        put(root, f"{dst}/{f.name}", html)
