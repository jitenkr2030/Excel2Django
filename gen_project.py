"""Generate settings, manage.py, commands, docs."""
from helpers import put

def generate_settings(root, P, A):
    put(root, "manage.py", "#!/usr/bin/env python3\nimport os,sys\nif __name__=='__main__':\n    os.environ.setdefault('DJANGO_SETTINGS_MODULE','"+P+".settings')\n    from django.core.management import execute_from_command_line\n    execute_from_command_line(sys.argv)\n")
    put(root, f"{P}/settings.py", S_TPL.replace("__A__",A).replace("__P__",P))
    put(root, f"{P}/urls.py", "from django.contrib import admin\nfrom django.urls import path,include\nfrom rest_framework.authtoken.views import obtain_auth_token\nfrom "+A+".api import router,register_api\nurlpatterns=[path('admin/',admin.site.urls),path('api/auth/token/',obtain_auth_token,name='api-token'),path('api/register/',register_api,name='api-register'),path('api/',include(router.urls)),path('',include('"+A+".urls'))]\n")
    put(root, f"{P}/wsgi.py", "import os\nfrom django.core.wsgi import get_wsgi_application\nos.environ.setdefault('DJANGO_SETTINGS_MODULE','"+P+".settings')\napplication=get_wsgi_application()\n")
    put(root, f"{P}/asgi.py", "import os\nfrom django.core.asgi import get_asgi_application\nos.environ.setdefault('DJANGO_SETTINGS_MODULE','"+P+".settings')\napplication=get_asgi_application()\n")
    put(root, f"{P}/__init__.py", "")
    put(root, f"{A}/__init__.py", "")
    put(root, f"{A}/templatetags/__init__.py", "")
    put(root, f"{A}/templatetags/portal_tags.py", "from django import template\nregister=template.Library()\n@register.filter\ndef lookup(obj,name):\n    return getattr(obj,name,'')\n")
    put(root, f"{A}/management/__init__.py", "")
    put(root, f"{A}/management/commands/__init__.py", "")
    (root / "logs").mkdir(exist_ok=True)
    put(root, "logs/app.log", "")
    put(root, f"{A}/middleware.py", MIDDLEWARE_CODE)
    print(f"  Settings generated for {P}")

S_TPL = """from pathlib import Path
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY="change-before-production"; DEBUG=True; ALLOWED_HOSTS=["*"]
INSTALLED_APPS=["django.contrib.admin","django.contrib.auth","django.contrib.contenttypes","django.contrib.sessions","django.contrib.messages","django.contrib.staticfiles","rest_framework","rest_framework.authtoken","__A__"]
MIDDLEWARE=["django.middleware.security.SecurityMiddleware","django.contrib.sessions.middleware.SessionMiddleware","django.middleware.common.CommonMiddleware","django.middleware.csrf.CsrfViewMiddleware","django.contrib.auth.middleware.AuthenticationMiddleware","django.contrib.messages.middleware.MessageMiddleware","django.middleware.clickjacking.XFrameOptionsMiddleware","__A__.middleware.RequestLogger"]
ROOT_URLCONF="__P__.urls"
TEMPLATES=[{"BACKEND":"django.template.backends.django.DjangoTemplates","DIRS":[],"APP_DIRS":True,"OPTIONS":{"context_processors":["django.template.context_processors.request","django.contrib.auth.context_processors.auth","django.contrib.messages.context_processors.messages"]}}]
WSGI_APPLICATION="__P__.wsgi.application"
DATABASES={"default":{"ENGINE":"django.db.backends.sqlite3","NAME":BASE_DIR/"db.sqlite3"}}
AUTH_USER_MODEL="__A__.User"
LOGIN_URL="/auth/login/"; LOGIN_REDIRECT_URL="/dashboard/"; LOGOUT_REDIRECT_URL="/"
LANGUAGE_CODE="en-us"; TIME_ZONE="Asia/Kolkata"; USE_I18N=True; USE_TZ=True
STATIC_URL="static/"; DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"
LOGGING={"version":1,"disable_existing_loggers":False,"formatters":{"verbose":{"format":"{asctime} {levelname} {name} {message}","style":"{","datefmt":"%Y-%m-%d %H:%M:%S"},"simple":{"format":"{levelname} {message}","style":"{"}},"handlers":{"console":{"class":"logging.StreamHandler","formatter":"verbose"},"file":{"class":"logging.handlers.RotatingFileHandler","filename":BASE_DIR/"logs/app.log","maxBytes":5242880,"backupCount":5,"formatter":"verbose"}},"loggers":{"django":{"handlers":["console","file"],"level":"INFO"},"__A__":{"handlers":["console","file"],"level":"INFO","propagate":False}}}
REST_FRAMEWORK={"DEFAULT_AUTHENTICATION_CLASSES":["rest_framework.authentication.TokenAuthentication","rest_framework.authentication.SessionAuthentication"],"DEFAULT_PERMISSION_CLASSES":["rest_framework.permissions.IsAuthenticated"],"DEFAULT_RENDERER_CLASSES":["rest_framework.renderers.JSONRenderer","rest_framework.renderers.BrowsableAPIRenderer"]}
"""

MIDDLEWARE_CODE = """import logging
import time

logger = logging.getLogger("portal")


class RequestLogger:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        duration = time.time() - start
        user = request.user.username if request.user.is_authenticated else "anon"
        logger.info(f"{request.method} {request.path} {response.status_code} {duration:.3f}s user={user}")
        return response
"""

def generate_commands(report, root, A):
    smap = "{" + ",".join('"%s":"%s"' % (i["sheet"], i["model"]) for i in report) + "}"
    cmd = 'from pathlib import Path\nfrom django.core.management.base import BaseCommand,CommandError\nfrom django.apps import apps\nfrom openpyxl import load_workbook\nSHEET_TO_MODEL=' + smap + '''
class Command(BaseCommand):
    help="Import Excel rows."
    def add_arguments(self,p):
        p.add_argument("path"); p.add_argument("--skip-existing",action="store_true")
    def handle(self,*a,**o):
        path=Path(o["path"])
        files=[path] if path.is_file() else sorted(p for p in path.iterdir() if p.suffix.lower() in(".xlsx",".xlsm") and not p.name.startswith("~$")) if path.is_dir() else []
        if not files: raise CommandError(f"Not found: {path}")
        for f in files:
            self.stdout.write(f"\\n{f.name}")
            wb=load_workbook(f,read_only=True,data_only=True)
            for ws in wb.worksheets:
                hdrs=next(ws.iter_rows(min_row=1,max_row=1,values_only=True),None)
                if not hdrs: continue
                mn=SHEET_TO_MODEL.get(ws.title)
                if not mn: self.stdout.write(self.style.WARNING(f"  [{ws.title}] skip")); continue
                model=apps.get_model("portal",mn)
                if o["skip_existing"] and model.objects.exists(): continue
                mf=[f.name for f in model._meta.fields if f.name!="id"]
                c=0
                for row in ws.iter_rows(min_row=2,values_only=True):
                    kw={}
                    for i in range(min(len(hdrs),len(mf))):
                        if i<len(row) and row[i] is not None: kw[mf[i]]=row[i]
                    try: model.objects.create(**kw); c+=1
                    except Exception as e: self.stdout.write(self.style.ERROR(f"  {e}"))
                self.stdout.write(self.style.SUCCESS(f"  [{mn}] {c} rows"))
            wb.close()
        self.stdout.write(self.style.SUCCESS("Done!"))
'''
    put(root, f"{A}/management/commands/import_excel.py", cmd)

def generate_docs(report, root, T):
    put(root, "requirements.txt", "Django>=4.2,<6.0\ndjangorestframework>=3.15,<4.0\nopenpyxl>=3.1\ngunicorn>=22\n")
    put(root, ".gitignore", "__pycache__/\n*.pyc\n.env\n.venv/\ndb.sqlite3\n.DS_Store\nlogs/\n")
    sr = ["# " + T + " Schema", ""]
    for i in report:
        sr += ["## " + i["sheet"] + " (" + i["model"] + ")", "- Rows: " + str(i["rows"])]
        sr += ["- `" + f["name"] + "` (" + f["type"] + ")" for f in i["fields"]]
        sr.append("")
    put(root, "SCHEMA_REPORT.md", "\n".join(sr))
    put(root, "README.md", "# " + T + "\n\n## Setup\n```\npip install -r requirements.txt\npython manage.py makemigrations portal && python manage.py migrate\npython manage.py createsuperuser\npython manage.py runserver 0.0.0.0:8000\n```\n")
