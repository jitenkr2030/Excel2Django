"""Shared utilities."""
import keyword, re
from pathlib import Path

_R = {"save","delete","objects","pk","meta","manager","does_not_exist","multiple_objects_returned"}

def slug(v):
    v = re.sub(r"[^a-zA-Z0-9]+","_",str(v or "").strip()).strip("_").lower() or "field"
    if v[0].isdigit(): v = "field_" + v
    if keyword.iskeyword(v) or v in _R: v += "_field"
    return v[:55]

def cname(v):
    n = "".join(x.capitalize() for x in re.findall(r"[A-Za-z0-9]+",str(v or "Record"))) or "Record"
    return ("Model"+n if n[0].isdigit() else n)[:65]

def put(root, name, text):
    p = Path(root) / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
