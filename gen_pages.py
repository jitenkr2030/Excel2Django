"""Domain detection and extra pages."""
from pathlib import Path
DOMAINS={"dating":["dating","match","swipe","love","partner","romance"],"creator":["creator","fan","tip","gift","stream","live","content","post"],"ecommerce":["product","order","cart","shop","store","merchandise"],"legal":["law","legal","case","court","lawyer"],"health":["health","medical","patient","doctor","appointment"],"finance":["loan","transaction","payment","payout","ledger"],"business":["business","employee","project","franchise","management"],"marketing":["marketing","campaign","lead","sales","customer"],"property":["property","construction","home","real","repair"],"skill":["skill","freelance","gig","worker","marketplace"]}
THEMES={
"dating":{"tag":"Find Your Perfect Match","sub":"Swipe, match, and find love.","c1":"Matching","c2":"Chat","c3":"Privacy","r1":"Man","r2":"Woman","r3":"Admin","i1":"&#9794;","i2":"&#9792;","i3":"&#9881;"},
"creator":{"tag":"Your Community. Your Business.","sub":"Content, tips, gifts, subscriptions.","c1":"Content","c2":"Payments","c3":"Analytics","r1":"Creator","r2":"Fan","r3":"Admin","i1":"&#127916;","i2":"&#9829;","i3":"&#9881;"},
"ecommerce":{"tag":"Shop. Sell. Grow.","sub":"Products, orders, and payments.","c1":"Products","c2":"Orders","c3":"Payments","r1":"Seller","r2":"Buyer","r3":"Admin","i1":"&#128722;","i2":"&#128717;","i3":"&#9881;"},
"legal":{"tag":"Legal Practice, Simplified.","sub":"Cases, clients, and billing.","c1":"Cases","c2":"Clients","c3":"Billing","r1":"Lawyer","r2":"Client","r3":"Admin","i1":"&#9878;","i2":"&#128188;","i3":"&#9881;"},
"health":{"tag":"Your Health, Your Way.","sub":"Appointments, records, and care.","c1":"Appointments","c2":"Records","c3":"Care","r1":"Doctor","r2":"Patient","r3":"Admin","i1":"&#129658;","i2":"&#128147;","i3":"&#9881;"},
"finance":{"tag":"Smart Finance, Simple.","sub":"Loans, transactions, payouts.","c1":"Loans","c2":"Transactions","c3":"Payouts","r1":"Lender","r2":"Borrower","r3":"Admin","i1":"&#128176;","i2":"&#128181;","i3":"&#9881;"},
"business":{"tag":"Run Your Business Better.","sub":"Team, projects, operations.","c1":"Team","c2":"Projects","c3":"Operations","r1":"Manager","r2":"Staff","r3":"Admin","i1":"&#128188;","i2":"&#128101;","i3":"&#9881;"},
"marketing":{"tag":"Grow Your Reach.","sub":"Campaigns, leads, analytics.","c1":"Campaigns","c2":"Leads","c3":"Analytics","r1":"Agency","r2":"Client","r3":"Admin","i1":"&#128226;","i2":"&#128188;","i3":"&#9881;"},
"property":{"tag":"Properties and Services.","sub":"Listings, construction, repairs.","c1":"Listings","c2":"Build","c3":"Repair","r1":"Agent","r2":"Client","r3":"Admin","i1":"&#127968;","i2":"&#128188;","i3":"&#9881;"},
"skill":{"tag":"Find and Hire Talent.","sub":"Skills, gigs, marketplace.","c1":"Talent","c2":"Gigs","c3":"Reviews","r1":"Worker","r2":"Employer","r3":"Admin","i1":"&#128736;","i2":"&#128188;","i3":"&#9881;"},
"general":{"tag":"Your Platform.","sub":"Complete data management.","c1":"Data","c2":"Analytics","c3":"Security","r1":"Member","r2":"Guest","r3":"Admin","i1":"&#128101;","i2":"&#128075;","i3":"&#9881;"}}

def detect(report,title):
    txt=(title+" "+" ".join(i["sheet"] for i in report)+" "+" ".join(i["model"] for i in report)).lower()
    sc={d:sum(1 for k in kws if k in txt) for d,kws in DOMAINS.items()}
    b=max(sc,key=sc.get); return b if sc[b]>0 else "general"

def generate_pages(report,root,A,T):
    dom=detect(report,T); th=THEMES.get(dom,THEMES["general"])
    B=Path(root)/A/"templates"/A
    for fn in ("index.html","about.html","register.html"):
        p=B/fn
        if p.exists():
            h=p.read_text(encoding="utf-8")
            h=h.replace("__TAG__",th["tag"]).replace("__SUB__",th["sub"])
            h=h.replace("__C1__",th["c1"]).replace("__C2__",th["c2"]).replace("__C3__",th["c3"])
            h=h.replace("__R1__",th["r1"]).replace("__R2__",th["r2"]).replace("__R3__",th["r3"])
            h=h.replace("__I1__",th["i1"]).replace("__I2__",th["i2"]).replace("__I3__",th["i3"])
            p.write_text(h,encoding="utf-8")
    vp=Path(root)/A/"views.py"
    vp.write_text(vp.read_text(encoding="utf-8")+EV,encoding="utf-8")
    up=Path(root)/A/"urls.py"
    s=up.read_text(encoding="utf-8")
    up.write_text(s.replace("    path('data/<str:model_name>/',","    path('about/',views.about,name='about'),\n    path('contact/',views.contact,name='contact'),\n    path('faq/',views.faq,name='faq'),\n    path('explore/',views.explore,name='explore'),\n    path('data/<str:model_name>/',"),encoding="utf-8")
    print(f"  Pages: domain={dom}, roles={th['r1']}/{th['r2']}/{th['r3']}")

EV="""

def about(request):
    return render(request,"portal/about.html",{"title":"About"})

def contact(request):
    if request.method=="POST":
        messages.success(request,"Message sent!"); return redirect("contact")
    return render(request,"portal/contact.html",{"title":"Contact"})

def faq(request):
    return render(request,"portal/faq.html",{"title":"FAQ","faqs":[{"q":"How do I start?","a":"Register and choose your role."},{"q":"Is it free?","a":"Yes."},{"q":"API?","a":"Get token at /api/auth/token/"}]})

@login_required_page
def explore(request):
    return render(request,"portal/explore.html",{"title":"Explore","stats":get_sidebar_stats()})
"""
