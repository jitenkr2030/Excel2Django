#!/usr/bin/env python3
"""
excel2frontend - Generate complete frontend from Excel worksheets.

Usage:
    python excel2frontend.py --input data.xlsx --output frontend/ --api http://localhost:8000

Works with any Excel file. Auto-detects domain and generates themed pages.
"""
import argparse, json, keyword, re, sys
from pathlib import Path
from openpyxl import load_workbook

R={"save","delete","objects","pk","meta","manager"}

def slug(v):
    v=re.sub(r"[^a-zA-Z0-9]+","_",str(v or "").strip()).strip("_").lower() or "field"
    if v[0].isdigit(): v="field_"+v
    if keyword.iskeyword(v) or v in R: v+="_field"
    return v[:55]

def cname(v):
    n="".join(x.capitalize() for x in re.findall(r"[A-Za-z0-9]+",str(v or "Record"))) or "Record"
    return ("Model"+n if n[0].isdigit() else n)[:65]

def analyse(src):
    src=Path(src)
    files=[src] if src.is_file() else sorted(p for p in src.iterdir() if p.suffix.lower() in(".xlsx",".xlsm") and not p.name.startswith("~$")) if src.is_dir() else []
    if not files: raise FileNotFoundError(f"Not found: {src}")
    result,used=[],set()
    for f in files:
        wb=load_workbook(f,read_only=True,data_only=True)
        for ws in wb.worksheets:
            hdrs=next(ws.iter_rows(min_row=1,max_row=1,values_only=True),None)
            if not hdrs: continue
            sample=list(ws.iter_rows(min_row=2,max_row=min(ws.max_row or 2,31),values_only=True))
            fields,uf=[],set()
            for i,raw in enumerate(hdrs):
                lab=str(raw or f"Col{i+1}").strip()
                fld=slug(lab); base,s=fld,2
                while fld in uf or fld=="id": fld,s=f"{base}_{s}",s+1
                uf.add(fld)
                vals=[r[i] for r in sample if i<len(r) and r[i] is not None]
                if vals and all(isinstance(v,bool) for v in vals): t="boolean"
                elif vals and all(isinstance(v,int) and not isinstance(v,bool) for v in vals): t="number"
                elif vals and all(isinstance(v,(int,float)) and not isinstance(v,bool) for v in vals): t="number"
                elif vals and all(hasattr(v,"year") for v in vals): t="date"
                else: t="text"
                fields.append({"name":fld,"label":lab,"type":t})
            bm=cname(ws.title); m,s=bm,2
            while m in used: m,s=f"{bm}{s}",s+1
            used.add(m)
            result.append({"sheet":ws.title,"model":m,"fields":fields,"rows":max((ws.max_row or 1)-1,0)})
        wb.close()
    return result

DOMAINS={"dating":["dating","match","swipe","love","partner","romance"],"creator":["creator","fan","tip","gift","stream","live","content","post"],"ecommerce":["product","order","cart","shop","store","merchandise"],"legal":["law","legal","case","court","lawyer"],"health":["health","medical","patient","doctor","appointment"],"finance":["loan","transaction","payment","payout","ledger"],"business":["business","employee","project","franchise","management"],"marketing":["marketing","campaign","lead","sales","customer"],"property":["property","construction","home","real","repair"],"skill":["skill","freelance","gig","worker","marketplace"]}
THEMES={"dating":{"tag":"Find Your Perfect Match","sub":"Swipe, match, and find love.","c1":"Matching","c2":"Chat","c3":"Privacy","clr":"#ff6b9d"},"creator":{"tag":"Your Community. Your Business.","sub":"Content, tips, gifts, subscriptions.","c1":"Content","c2":"Payments","c3":"Analytics","clr":"#b9f477"},"ecommerce":{"tag":"Shop. Sell. Grow.","sub":"Products, orders, and payments.","c1":"Products","c2":"Orders","c3":"Payments","clr":"#f59e0b"},"legal":{"tag":"Legal Practice, Simplified.","sub":"Cases, clients, and billing.","c1":"Cases","c2":"Clients","c3":"Billing","clr":"#818cf8"},"health":{"tag":"Your Health, Your Way.","sub":"Appointments, records, and care.","c1":"Appointments","c2":"Records","c3":"Care","clr":"#34d399"},"finance":{"tag":"Smart Finance, Simple.","sub":"Loans, transactions, payouts.","c1":"Loans","c2":"Transactions","c3":"Payouts","clr":"#60a5fa"},"business":{"tag":"Run Your Business Better.","sub":"Team, projects, operations.","c1":"Team","c2":"Projects","c3":"Operations","clr":"#b9f477"},"marketing":{"tag":"Grow Your Reach.","sub":"Campaigns, leads, analytics.","c1":"Campaigns","c2":"Leads","c3":"Analytics","clr":"#f472b6"},"property":{"tag":"Properties and Services.","sub":"Listings, construction, repairs.","c1":"Listings","c2":"Build","c3":"Repair","clr":"#fbbf24"},"skill":{"tag":"Find and Hire Talent.","sub":"Skills, gigs, marketplace.","c1":"Talent","c2":"Gigs","c3":"Reviews","clr":"#a78bfa"},"general":{"tag":"Your Platform.","sub":"Complete data management.","c1":"Data","c2":"Analytics","c3":"Security","clr":"#b9f477"}}

def detect(report,title):
    txt=(title+" "+" ".join(i["sheet"] for i in report)+" "+" ".join(i["model"] for i in report)).lower()
    sc={d:sum(1 for k in kws if k in txt) for d,kws in DOMAINS.items()}
    b=max(sc,key=sc.get); return b if sc[b]>0 else "general"

def generate(report,output,title,api):
    out=Path(output)
    out.mkdir(parents=True,exist_ok=True)
    dom=detect(report,title)
    th=THEMES.get(dom,THEMES["general"])
    tpl=Path(__file__).parent/"frontend_tpl"
    models_json=json.dumps([{ "name":i["model"],"sheet":i["sheet"],"fields":i["fields"],"rows":i["rows"]} for i in report])
    for f in tpl.glob("*"):
        html=f.read_text(encoding="utf-8")
        html=html.replace("__TITLE__",title).replace("__TAG__",th["tag"]).replace("__SUB__",th["sub"])
        html=html.replace("__C1__",th["c1"]).replace("__C2__",th["c2"]).replace("__C3__",th["c3"])
        html=html.replace("__CLR__",th["clr"]).replace("__DOMAIN__",dom).replace("__API__",api)
        html=html.replace("__MODELS__",models_json).replace("__COUNT__",str(len(report)))
        (out/f.name).write_text(html,encoding="utf-8")
    print(f"Frontend generated: {out}")
    print(f"Domain: {dom} | Theme: {th['tag']} | Color: {th['clr']}")
    print(f"Models: {', '.join(i['model'] for i in report)}")
    print(f"Open: {out/'index.html'}")

def main():
    p=argparse.ArgumentParser(description="Generate frontend from Excel")
    p.add_argument("--input",required=True)
    p.add_argument("--output",default="frontend")
    p.add_argument("--title",default="My Platform")
    p.add_argument("--api",default="http://localhost:8000")
    a=p.parse_args()
    try:
        report=analyse(a.input)
        print(f"Found {len(report)} worksheets")
        generate(report,a.output,a.title,a.api)
    except Exception as e:
        print(f"ERROR: {e}",file=sys.stderr); sys.exit(1)

if __name__=="__main__": main()
