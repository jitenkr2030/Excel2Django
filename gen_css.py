"""Generate domain-aware themed CSS."""
from helpers import put
from gen_pages import detect, THEMES

PALETTES={
"dating":{"primary":"#ff6b9d","bg":"#0c0812","card":"#1a1025","border":"#2d1f3e","accent":"#ff8fb8","muted":"#9c8aa8","grad":"radial-gradient(circle at 70% 20%,#2d1040,#0c0812 70%)","font":"'Playfair Display',serif"},
"creator":{"primary":"#b9f477","bg":"#080c18","card":"#121b2e","border":"#27334a","accent":"#d4ff9e","muted":"#9caac2","grad":"radial-gradient(circle at 70% 20%,#1a2a42,#080c18 70%)","font":"Inter,system-ui"},
"ecommerce":{"primary":"#f59e0b","bg":"#120e06","card":"#1e1810","border":"#3d2f14","accent":"#fbbf24","muted":"#b8a078","grad":"radial-gradient(circle at 70% 20%,#2e2210,#120e06 70%)","font":"Inter,system-ui"},
"legal":{"primary":"#818cf8","bg":"#080a14","card":"#12152e","border":"#272d4a","accent":"#a5b4fc","muted":"#8890b0","grad":"radial-gradient(circle at 70% 20%,#1a1e3e,#080a14 70%)","font":"'Merriweather',serif"},
"health":{"primary":"#34d399","bg":"#061210","card":"#0e2420","border":"#1a3d35","accent":"#6ee7b7","muted":"#7cb8a5","grad":"radial-gradient(circle at 70% 20%,#0e2e28,#061210 70%)","font":"Inter,system-ui"},
"finance":{"primary":"#60a5fa","bg":"#060c18","card":"#0e1a2e","border":"#1a2d4a","accent":"#93c5fd","muted":"#7a9cc0","grad":"radial-gradient(circle at 70% 20%,#102040,#060c18 70%)","font":"Inter,system-ui"},
"business":{"primary":"#b9f477","bg":"#0c0e06","card":"#181e0e","border":"#2a3320","accent":"#d4ff9e","muted":"#9cac78","grad":"radial-gradient(circle at 70% 20%,#1e2810,#0c0e06 70%)","font":"Inter,system-ui"},
"marketing":{"primary":"#f472b6","bg":"#120812","card":"#201020","border":"#3d1a3d","accent":"#f9a8d4","muted":"#b080a0","grad":"radial-gradient(circle at 70% 20%,#2a1030,#120812 70%)","font":"Inter,system-ui"},
"property":{"primary":"#fbbf24","bg":"#120e04","card":"#201808","border":"#3d2d10","accent":"#fcd34d","muted":"#c0a060","grad":"radial-gradient(circle at 70% 20%,#2e2010,#120e04 70%)","font":"Inter,system-ui"},
"skill":{"primary":"#a78bfa","bg":"#0c0814","card":"#181028","border":"#2d1f42","accent":"#c4b5fd","muted":"#9880b8","grad":"radial-gradient(circle at 70% 20%,#1e1038,#0c0814 70%)","font":"Inter,system-ui"},
"general":{"primary":"#b9f477","bg":"#080c18","card":"#121b2e","border":"#27334a","accent":"#d4ff9e","muted":"#9caac2","grad":"radial-gradient(circle at 70% 20%,#1a2a42,#080c18 70%)","font":"Inter,system-ui"}}

VARS = ":root{--clr:__P__;--bg:__B__;--card:__C__;--border:__BR__;--accent:__A__;--text:__T__;--muted:__M__;--grad:__G__}"

def generate_all(report, root, A, T):
    dom = detect(report, T)
    p = PALETTES.get(dom, PALETTES["general"])
    vars_css = (VARS.replace("__P__",p["primary"]).replace("__B__",p["bg"])
        .replace("__C__",p["card"]).replace("__BR__",p["border"])
        .replace("__A__",p["accent"]).replace("__T__","#edf2ff")
        .replace("__M__",p["muted"]).replace("__G__",p["grad"]))
    style = vars_css + BODY(p) + SIDEBAR(p) + MAIN(p) + HERO(p) + TABLES(p) + FORMS(p) + MOBILE()
    landing = vars_css + BODY(p) + NAV(p) + LANHERO(p) + FEATURES(p) + STATS(p) + CTA(p) + AUTH(p) + FOOTER(p) + LANMOBILE()
    put(root, f"{A}/static/{A}/style.css", style)
    put(root, f"{A}/static/{A}/landing.css", landing)
    print(f"  CSS: domain={dom}, primary={p['primary']}, font={p['font']}")

def BODY(p):
    return f"\n*{{box-sizing:border-box;margin:0;padding:0}}body{{background:var(--bg);color:var(--text);font-family:{p['font']};font-size:15px;line-height:1.6}}a{{color:inherit;text-decoration:none}}img{{max-width:100%}}"

def SIDEBAR(p):
    c,b,br,m=p["card"],p["bg"],p["border"],p["muted"]
    return f"""
.sidebar{{position:fixed;left:0;top:0;bottom:0;width:240px;background:{c};border-right:1px solid {br};padding:1.5rem 1rem;overflow-y:auto;z-index:100}}
.sidebar .brand{{display:block;font-size:1.4rem;font-weight:900;margin-bottom:2rem}}.sidebar .brand span{{color:var(--clr)}}
.sidebar p{{font-size:.65rem;letter-spacing:2px;text-transform:uppercase;color:{m};margin:.5rem 0 .75rem;font-weight:800}}
.sidebar a{{display:block;padding:.65rem .85rem;border-radius:.5rem;color:{m};font-size:.9rem;transition:.2s;margin-bottom:.15rem}}
.sidebar a:hover,.sidebar a.active{{background:rgba(255,255,255,.05);color:var(--text)}}
.sidebar a small{{color:var(--clr);font-size:.75rem;float:right}}
.sidefoot{{padding-top:1.5rem;border-top:1px solid {br};margin-top:2rem}}.sidefoot a{{display:inline-block;font-size:.85rem}}
.logout-link{{color:#e74c3c!important}}"""

def MAIN(p):
    br,m=p["border"],p["muted"]
    return f"""
main{{margin-left:240px;min-height:100vh}}.auth-main{{margin-left:0}}
.topbar{{height:56px;border-bottom:1px solid {br};display:flex;align-items:center;padding:0 1.5rem;gap:1rem;position:sticky;top:0;background:var(--bg);z-index:50}}
.topbar span{{font-weight:700;color:{m}}}
.user-area{{margin-left:auto;display:flex;align-items:center;gap:.75rem}}
.role-badge{{padding:.25rem .75rem;border-radius:2rem;font-size:.7rem;font-weight:800;text-transform:uppercase}}
.role-badge.role-admin{{background:rgba(231,76,60,.15);color:#e74c3c}}.role-badge.role-creator{{background:rgba(185,244,119,.15);color:#b9f477}}.role-badge.role-client{{background:rgba(52,152,219,.15);color:#3498db}}
.avatar{{width:36px;height:36px;border-radius:50%;background:var(--clr);color:var(--bg);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:.9rem}}
.menu-toggle{{display:none;background:none;border:0;color:var(--text);font-size:1.25rem;cursor:pointer}}
.messages{{padding:.75rem 1.5rem}}.msg{{padding:.75rem 1rem;border-radius:.5rem;margin-bottom:.5rem;font-size:.9rem}}
.msg-success{{background:rgba(52,195,90,.1);color:#2ecc71;border:1px solid rgba(52,195,90,.2)}}.msg-error{{background:rgba(231,76,60,.1);color:#e74c3c;border:1px solid rgba(231,76,60,.2)}}
.heading{{display:flex;align-items:center;justify-content:space-between;margin-bottom:1.5rem;flex-wrap:wrap;gap:1rem}}.heading h1{{font-size:1.75rem;font-weight:900}}
.eyebrow{{font-size:.65rem;letter-spacing:3px;font-weight:800;color:var(--clr);text-transform:uppercase;margin-bottom:.5rem}}.muted{{color:{m};margin-top:.5rem}}
.button,.btn{{padding:.75rem 1.5rem;border-radius:.5rem;font-weight:700;cursor:pointer;border:0;display:inline-block;transition:.2s;font-size:.95rem;background:var(--clr);color:var(--bg)}}
.button.secondary{{background:rgba(255,255,255,.08);color:var(--text)}}.btn-danger{{background:#e74c3c;color:#fff}}
.btn-sm{{padding:.35rem .75rem;border-radius:.35rem;font-size:.75rem;font-weight:700;background:rgba(255,255,255,.08);color:var(--text);display:inline-block;cursor:pointer}}
.btn-edit{{background:rgba(52,152,219,.15);color:#3498db}}.btn-delete{{background:rgba(231,76,60,.15);color:#e74c3c}}
.quick-actions{{display:flex;flex-wrap:wrap;gap:.75rem;margin-bottom:1.5rem}}
.stats{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:1rem;margin-bottom:2rem}}
.card{{background:var(--card);border:1px solid {br};border-radius:1rem;padding:1.25rem;transition:.2s}}.card:hover{{border-color:var(--clr)}}
.card span{{display:block;color:{m};font-size:.85rem}}.card strong{{display:block;font-size:1.75rem;margin:.25rem 0}}.card small{{color:var(--clr);font-size:.75rem}}
.panel{{background:var(--card);border:1px solid {br};border-radius:1rem;padding:1.5rem;margin-bottom:1.5rem}}.panel h2{{font-size:1.15rem;font-weight:800;margin-bottom:1rem}}
.pagination{{display:flex;align-items:center;gap:1rem;color:{m};font-size:.9rem}}.pagination a{{color:var(--clr);font-weight:600}}"""

def HERO(p):
    c,br,m=p["card"],p["border"],p["muted"]
    return f"""
.hero{{display:flex;align-items:center;justify-content:space-between;padding:2.5rem;background:var(--grad);border-radius:1.25rem;margin-bottom:2rem;border:1px solid {br}}}
.hero h1{{font-size:2.5rem;font-weight:900;line-height:1.15;letter-spacing:-1px}}.hero h1 span{{color:var(--clr)}}
.mark{{width:100px;height:100px;border-radius:1.5rem;background:var(--clr);color:var(--bg);display:flex;align-items:center;justify-content:center;font-size:2.5rem;font-weight:900;flex-shrink:0}}
.mark span{{color:var(--bg);opacity:.5}}"""

def TABLES(p):
    br,pri=p["border"],p["primary"]
    return f"""
.tablewrap{{overflow-x:auto;background:var(--card);border:1px solid {br};border-radius:1rem;margin-bottom:1.5rem}}
table{{width:100%;border-collapse:collapse}}
th{{background:rgba(255,255,255,.03);color:var(--muted);font-size:.7rem;text-transform:uppercase;letter-spacing:1px;padding:.75rem 1rem;text-align:left;white-space:nowrap}}
td{{padding:.75rem 1rem;border-bottom:1px solid {br};font-size:.9rem}}
tr:hover{{background:rgba(255,255,255,.02)}}
.detail-table th{{width:200px;background:rgba(255,255,255,.03)}}.detail-table td{{color:var(--text)}}
.delete-panel{{border-color:rgba(231,76,60,.3)}}
.search{{display:flex;gap:.75rem;margin-bottom:1.5rem}}
.search input{{flex:1;padding:.75rem 1rem;border-radius:.5rem;border:1px solid {br};background:var(--card);color:var(--text);outline:none}}.search input:focus{{border-color:{pri}}}"""

def FORMS(p):
    br,pri=p["border"],p["primary"]
    return f"""
.form-grid{{display:grid;gap:1.25rem}}
.form-group label{{display:block;font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:var(--muted);margin-bottom:.5rem}}
.form-group input,.form-group select,.form-group textarea{{width:100%;padding:.75rem 1rem;border-radius:.5rem;border:1px solid {br};background:var(--card);color:var(--text);outline:none;font-size:.95rem}}
.form-group input:focus{{border-color:{pri}}}
.field-errors{{color:#e74c3c;font-size:.8rem;margin-top:.35rem}}
.form-actions{{display:flex;gap:.75rem;margin-top:1rem}}"""

def MOBILE():
    return """
@media(max-width:768px){.sidebar{transform:translateX(-100%);transition:.3s}.sidebar.open{transform:translateX(0)}
main{margin-left:0}.menu-toggle{display:block}.hero{flex-direction:column;text-align:center}.mark{margin-top:1rem}
.stats{grid-template-columns:repeat(auto-fill,minmax(150px,1fr))}}"""

def NAV(p):
    br,m=p["border"],p["muted"]
    return f"""
.landing-nav,.auth-nav{{position:fixed;top:0;left:0;right:0;z-index:100;display:flex;align-items:center;justify-content:space-between;padding:1rem 2rem;background:rgba(8,12,24,.9);backdrop-filter:blur(12px);border-bottom:1px solid {br}}}
.nav-brand{{font-size:1.35rem;font-weight:900}}.nav-brand span{{color:var(--clr)}}
.nav-links{{display:flex;align-items:center;gap:1.5rem}}.nav-links a{{color:{m};font-size:.9rem;transition:.2s}}.nav-links a:hover{{color:var(--text)}}
.btn-nav{{padding:.55rem 1.25rem!important;border-radius:.5rem;background:var(--clr);color:var(--bg)!important;font-weight:700}}"""

def LANHERO(p):
    return """
.hero-section{padding:10rem 2rem 5rem;display:flex;align-items:center;justify-content:space-between;max-width:1200px;margin:0 auto;gap:3rem}
.hero-content{max-width:550px}
.hero-eyebrow{font-size:.7rem;letter-spacing:3px;font-weight:800;color:var(--clr);text-transform:uppercase;margin-bottom:1rem}
.hero-content h1{font-size:clamp(2.5rem,5vw,4rem);font-weight:900;line-height:1.1;letter-spacing:-2px}
.hero-content h1 span{color:var(--clr)}
.hero-sub{color:var(--muted);font-size:1.15rem;margin-top:1.25rem}
.hero-buttons{display:flex;gap:1rem;margin-top:2rem}
.btn-primary{padding:.85rem 2rem;border-radius:.5rem;background:var(--clr);color:var(--bg);font-weight:800;font-size:1rem;transition:.2s}
.btn-outline{padding:.85rem 2rem;border-radius:.5rem;border:2px solid var(--border);color:var(--text);font-weight:700;font-size:1rem;transition:.2s}
.btn-outline:hover{border-color:var(--clr);color:var(--clr)}
.btn-large{padding:1rem 2.5rem!important;font-size:1.15rem!important}
.hero-visual{display:flex;flex-direction:column;gap:1rem}
.hero-card{background:var(--card);border:1px solid var(--border);border-radius:1rem;padding:1.25rem 1.5rem;display:flex;align-items:center;gap:1rem;transition:.3s}
.hero-card:hover{transform:translateX(-8px);border-color:var(--clr)}
.hc-icon{width:48px;height:48px;border-radius:.75rem;display:flex;align-items:center;justify-content:center;font-size:1.35rem;flex-shrink:0}
.card-1 .hc-icon{background:rgba(255,107,157,.15);color:#ff6b9d}.card-2 .hc-icon{background:rgba(185,244,119,.15);color:#b9f477}.card-3 .hc-icon{background:rgba(52,152,219,.15);color:#3498db}
.hero-card h3{font-size:.95rem;font-weight:700}.hero-card p{color:var(--muted);font-size:.8rem}"""

def FEATURES(p):
    return """
.features-section{padding:5rem 2rem;max-width:1200px;margin:0 auto;text-align:center}
.section-eyebrow{font-size:.65rem;letter-spacing:3px;font-weight:800;color:var(--clr);text-transform:uppercase;margin-bottom:.75rem}
.features-section h2{font-size:2.25rem;font-weight:900;margin-bottom:3rem}
.features-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:1.5rem;text-align:left}
.feature-card{background:var(--card);border:1px solid var(--border);border-radius:1rem;padding:1.75rem;transition:.2s}
.feature-card:hover{border-color:var(--clr);transform:translateY(-4px)}
.fi{font-size:2rem;margin-bottom:.75rem}
.feature-card h3{font-size:1.1rem;font-weight:800;margin-bottom:.5rem}.feature-card p{color:var(--muted);font-size:.9rem}"""

def STATS(p):
    return """
.stats-section{display:grid;grid-template-columns:repeat(4,1fr);gap:1.5rem;max-width:900px;margin:0 auto;padding:2rem}
.stat{text-align:center;background:var(--card);border:1px solid var(--border);border-radius:1rem;padding:2rem}
.stat strong{display:block;font-size:2.5rem;color:var(--clr);font-weight:900}.stat span{color:var(--muted);font-size:.85rem;text-transform:uppercase;letter-spacing:1px}"""

def CTA(p):
    return """
.cta-section{padding:5rem 2rem;text-align:center;background:var(--grad)}
.cta-section h2{font-size:2.5rem;font-weight:900;margin-bottom:1rem}
.cta-section p{color:var(--muted);margin-bottom:2rem;font-size:1.15rem}"""

def AUTH(p):
    br,m,pri=p["border"],p["muted"],p["primary"]
    return f"""
.auth-page{{min-height:100vh;display:flex;flex-direction:column}}
.auth-main-area{{flex:1;display:flex;align-items:center;justify-content:center;padding:6rem 2rem 2rem}}
.auth-box{{width:100%;max-width:480px;background:var(--card);border:1px solid {br};border-radius:1.25rem;padding:2.5rem}}
.auth-icon{{font-size:3rem;text-align:center;margin-bottom:.5rem}}
.auth-box h2{{font-size:1.75rem;font-weight:900;text-align:center}}
.subtitle{{text-align:center;color:{m};margin-bottom:1.5rem}}
.auth-form{{display:flex;flex-direction:column;gap:1.15rem}}
.auth-field label{{display:block;font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:{m};margin-bottom:.5rem}}
.auth-field input,.auth-field textarea{{width:100%;padding:.85rem 1rem;border-radius:.5rem;border:1px solid {br};background:var(--bg);color:var(--text);outline:none;font-size:.95rem}}
.auth-field input:focus{{border-color:{pri}}}
.form-row{{display:grid;grid-template-columns:1fr 1fr;gap:1rem}}
.auth-btn{{padding:.85rem 1.5rem;border-radius:.5rem;background:var(--clr);color:var(--bg);font-weight:800;font-size:1rem;border:0;cursor:pointer;width:100%}}
.divider{{text-align:center;color:{m};font-size:.85rem;margin:1.5rem 0;position:relative}}.divider::before{{content:'';position:absolute;left:0;right:0;top:50%;height:1px;background:{br}}}.divider{{background:var(--card);display:inline-block;padding:0 .75rem;margin:1.5rem auto;display:block;width:fit-content}}
.auth-links{{text-align:center;color:{m}}}.auth-links a{{color:{pri};font-weight:700}}
.error-msg{{background:rgba(231,76,60,.1);color:#e74c3c;padding:.75rem;border-radius:.5rem;font-size:.85rem;text-align:center}}
.success-msg{{background:rgba(46,204,113,.1);color:#2ecc71;padding:.75rem;border-radius:.5rem;font-size:.85rem;text-align:center}}
.role-section{{margin-top:.25rem}}.role-section label{{display:block;font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:{m};margin-bottom:.75rem}}
.role-option{{display:flex;gap:.75rem}}
.role-pill{{flex:1;display:flex;flex-direction:column;align-items:center;gap:.35rem;padding:.85rem;border-radius:.75rem;border:2px solid {br};cursor:pointer;transition:.2s;text-align:center}}
.role-pill input{{display:none}}.role-pill:hover{{border-color:{pri}}}
.role-pill:has(input:checked){{border-color:{pri};background:rgba(255,255,255,.03)}}
.role-icon{{font-size:1.5rem}}
.footer-note{{text-align:center;padding:1.5rem;color:{m};font-size:.85rem}}"""

def FOOTER(p):
    br,m=p["border"],p["muted"]
    return f"""
.landing-footer{{padding:3rem 2rem;border-top:1px solid {br};max-width:1200px;margin:0 auto}}
.footer-grid{{display:grid;grid-template-columns:2fr 1fr 1fr;gap:2rem;margin-bottom:2rem}}
.footer-grid h4{{font-size:1.25rem;font-weight:900}}.footer-grid h4 span{{color:var(--clr)}}
.footer-grid h5{{color:{m};font-size:.75rem;letter-spacing:2px;text-transform:uppercase;margin-bottom:.75rem}}
.footer-grid a,.footer-grid span{{display:block;color:{m};margin-bottom:.5rem;font-size:.9rem;transition:.2s}}
.footer-grid a:hover{{color:var(--text)}}
.copyright{{text-align:center;color:{m};font-size:.85rem;padding-top:2rem;border-top:1px solid {br}}}"""

def LANMOBILE():
    return """
@media(max-width:768px){
.hero-section{flex-direction:column;padding:8rem 1.5rem 3rem;text-align:center}
.hero-visual{display:none}.features-grid{grid-template-columns:1fr}
.stats-section{grid-template-columns:repeat(2,1fr)}.footer-grid{grid-template-columns:1fr}
.nav-links{gap:1rem}.nav-links a{font-size:.8rem}.form-row{grid-template-columns:1fr}}"""

# Phase 2: Loading, Toasts, Sorting, Upload CSS
EXTRA_CSS = """
/* Theme toggle */
.theme-toggle{background:none;border:1px solid var(--border);border-radius:.5rem;padding:.45rem .75rem;cursor:pointer;font-size:1rem;color:var(--text);transition:.2s}
.theme-toggle:hover{border-color:var(--clr)}
[data-theme="light"]{--bg:#f0f2f5;--text:#1a1a2e;--card:#ffffff;--border:#d1d5db;--muted:#6b7280}
[data-theme="light"] .sidebar{background:#ffffff;border-right-color:#e5e7eb}
[data-theme="light"] .topbar{background:#ffffff;border-bottom-color:#e5e7eb}
[data-theme="light"] .hero{background:linear-gradient(135deg,#e8f5e9,#f3e5f5)}
[data-theme="light"] th{background:#f9fafb}
[data-theme="light"] td{border-bottom-color:#e5e7eb}
[data-theme="light"] .auth-field input{background:#f9fafb;color:#1a1a2e;border-color:#d1d5db}
[data-theme="light"] .card{background:#ffffff;border-color:#e5e7eb}
[data-theme="light"] .panel{background:#ffffff;border-color:#e5e7eb}
[data-theme="light"] .search input{background:#f9fafb;color:#1a1a2e;border-color:#d1d5db}
[data-theme="light"] .form-group input,[data-theme="light"] .form-group textarea{background:#f9fafb;color:#1a1a2e;border-color:#d1d5db}

/* Breadcrumbs */
.breadcrumbs{display:flex;align-items:center;gap:.5rem;font-size:.85rem;color:var(--muted)}
.breadcrumbs a{color:var(--clr);text-decoration:none}
.breadcrumbs span{opacity:.5}

/* Loading spinner */
.spinner-overlay{position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(8,12,24,.7);z-index:9999;display:flex;align-items:center;justify-content:center}
.spinner{width:48px;height:48px;border:4px solid var(--border);border-top-color:var(--clr);border-radius:50%;animation:spin .8s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.loading-bar{height:3px;background:var(--clr);width:100%;animation:load 1.5s ease-in-out infinite;position:fixed;top:0;z-index:9999}
@keyframes load{0%{width:0%}50%{width:70%}100%{width:100%}}

/* Toast notifications */
.toast-container{position:fixed;top:70px;right:1.5rem;z-index:9000;display:flex;flex-direction:column;gap:.5rem;max-width:380px}
.toast{padding:.85rem 1.25rem;border-radius:.75rem;font-size:.9rem;font-weight:600;display:flex;align-items:center;gap:.75rem;animation:slideIn .3s ease;box-shadow:0 8px 30px rgba(0,0,0,.3);cursor:pointer}
.toast-success{background:rgba(46,204,113,.15);color:#2ecc71;border:1px solid rgba(46,204,113,.3)}
.toast-error{background:rgba(231,76,60,.15);color:#e74c3c;border:1px solid rgba(231,76,60,.3)}
.toast-info{background:rgba(52,152,219,.15);color:#3498db;border:1px solid rgba(52,152,219,.3)}
.toast-warning{background:rgba(245,166,35,.15);color:#f39c12;border:1px solid rgba(245,166,35,.3)}
@keyframes slideIn{from{transform:translateX(100%);opacity:0}to{transform:translateX(0);opacity:1}}

/* Sortable table headers */
th.sortable{cursor:pointer;user-select:none;transition:.2s}
th.sortable:hover{color:var(--clr)}
th.sortable::after{content:' \\2195';opacity:.3;font-size:.6rem}
th.sortable.asc::after{content:' \\2191';opacity:1;color:var(--clr)}
th.sortable.desc::after{content:' \\2193';opacity:1;color:var(--clr)}

/* File upload */
.file-upload{border:2px dashed var(--border);border-radius:.75rem;padding:2rem;text-align:center;cursor:pointer;transition:.2s}
.file-upload:hover{border-color:var(--clr);background:rgba(255,255,255,.02)}
.file-upload.has-file{border-color:var(--clr);background:rgba(185,244,119,.05)}
.file-upload-icon{font-size:2.5rem;margin-bottom:.5rem;opacity:.5}
.file-upload input{display:none}
.file-preview{margin-top:1rem;display:flex;align-items:center;gap:.75rem;padding:.75rem;background:rgba(255,255,255,.03);border-radius:.5rem}
.file-preview .name{flex:1;font-size:.85rem;color:var(--muted)}
.file-preview .remove{color:#e74c3c;cursor:pointer;font-size:.85rem;font-weight:700}

/* Auth guard overlay */
.auth-overlay{position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(8,12,24,.95);z-index:8000;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:1.5rem}
.auth-overlay h2{font-size:1.5rem;font-weight:900}
"""

def generate_all(report, root, A, T):
    dom = detect(report, T)
    p = PALETTES.get(dom, PALETTES["general"])
    vars_css = (VARS.replace("__P__",p["primary"]).replace("__B__",p["bg"])
        .replace("__C__",p["card"]).replace("__BR__",p["border"])
        .replace("__A__",p["accent"]).replace("__T__","#edf2ff")
        .replace("__M__",p["muted"]).replace("__G__",p["grad"]))
    style = vars_css + BODY(p) + SIDEBAR(p) + MAIN(p) + HERO(p) + TABLES(p) + FORMS(p) + EXTRA_CSS + MOBILE()
    landing = vars_css + BODY(p) + NAV(p) + LANHERO(p) + FEATURES(p) + STATS(p) + CTA(p) + AUTH(p) + FOOTER(p) + EXTRA_CSS + LANMOBILE()
    put(root, f"{A}/static/{A}/style.css", style)
    put(root, f"{A}/static/{A}/landing.css", landing)
    print(f"  CSS: domain={dom}, primary={p['primary']}, font={p['font']}")
