"""Generate models, admin, forms with validation."""
from helpers import put

def generate_models(report, root, A):
    ml = [
        "from django.contrib.auth.models import AbstractUser",
        "from django.db import models",
        "", "",
        "class User(AbstractUser):",
        "    ROLE_CHOICES = [('admin','Admin'),('creator','Creator'),('client','Client')]",
        "    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')",
        "", "    class Meta:", "        verbose_name = 'User'", "        verbose_name_plural = 'Users'", "",
        "    @property", "    def is_admin_role(self):", "        return self.role == 'admin' or self.is_superuser", "",
        "    @property", "    def is_creator_role(self):", "        return self.role == 'creator'", "",
        "    @property", "    def is_client_role(self):", "        return self.role == 'client'", "",
        "    def __str__(self):", "        return f'{self.username} ({self.role})'", "", "",
    ]
    for item in report:
        m = item["model"]
        ml.append(f"class {m}(models.Model):")
        if not item["fields"]:
            ml.append("    pass")
        for f in item["fields"]:
            lab = f["label"].replace("'", "\\'")
            if f["type"] == "TextField":
                d = f"models.TextField(verbose_name='{lab}', blank=True, default='', max_length=5000)"
            elif f["type"] == "DateField":
                d = f"models.DateField(verbose_name='{lab}', null=True, blank=True)"
            elif f["type"] == "IntegerField":
                d = f"models.IntegerField(verbose_name='{lab}', null=True, blank=True, default=0)"
            else:
                d = f"models.CharField(verbose_name='{lab}', max_length=255, null=True, blank=True, default='')"
            ml.append(f"    {f['name']} = {d}")
        ml += [
            "", "    class Meta:",
            f"        verbose_name = '{m}'",
            f"        verbose_name_plural = '{m} Items'",
            "        ordering = ['-id']",
            "        indexes = [models.Index(fields=['-id'])]",
            "", "    def __str__(self):",
            f"        return str(self.{item['fields'][0]['name']})" if item["fields"] else f"        return '{m} object'",
            "",
            "    def clean(self):",
            "        from django.core.exceptions import ValidationError",
            "        super().clean()",
            "        errors = {}",
            f"        if hasattr(self, '{item['fields'][0]['name']}') and item['fields'][0]['type'] == 'text' if False else True:",
            "            pass",
            "        if errors: raise ValidationError(errors)",
            "", "",
        ]
    put(root, f"{A}/models.py", "\n".join(ml))

def generate_admin(report, root, A):
    names = [i["model"] for i in report]
    mi = "from .models import User" + (", " + ", ".join(names) if names else "")
    al = [
        "from django.contrib import admin",
        "from django.contrib.auth.admin import UserAdmin as BaseUserAdmin",
        mi, "", "",
        "@admin.register(User)",
        "class UserAdmin(BaseUserAdmin):",
        "    list_display = ('username', 'email', 'role', 'is_active', 'is_staff', 'date_joined')",
        "    list_filter = ('role', 'is_active', 'is_staff')",
        "    search_fields = ('username', 'email', 'first_name', 'last_name')",
        "    fieldsets = BaseUserAdmin.fieldsets + (('Role', {'fields': ('role',)}),)",
        "    add_fieldsets = BaseUserAdmin.add_fieldsets + (('Role', {'fields': ('role',)}),)",
    ]
    for item in report:
        m = item["model"]
        fn = [f["name"] for f in item["fields"][:5]]
        ld = ", ".join("'"+n+"'" for n in fn)
        sf = ", ".join("'"+n+"'" for n in fn[:3])
        al += [
            "", "",
            f"@admin.register({m})",
            f"class {m}Admin(admin.ModelAdmin):",
            "    list_display = ('id', " + ld + ")",
        ]
        if sf:
            al.append("    search_fields = (" + sf + ",)")
        al += ["    list_per_page = 25", "    list_filter = ()"]
    put(root, f"{A}/admin.py", "\n".join(al))

def generate_forms(report, root, A):
    names = [i["model"] for i in report]
    mi = "from .models import User" + (", " + ", ".join(names) if names else "")
    fl = [
        "from django import forms",
        "from django.core.exceptions import ValidationError",
        "from django.contrib.auth.forms import UserCreationForm",
        mi, "", "",
        "class RegisterForm(UserCreationForm):",
        "    email = forms.EmailField(required=True)",
        "    role = forms.ChoiceField(choices=User.ROLE_CHOICES, initial='client')",
        "",
        "    class Meta:",
        "        model = User",
        "        fields = ('username', 'email', 'first_name', 'last_name', 'role', 'password1', 'password2')",
        "",
        "    def clean_email(self):",
        "        email = self.cleaned_data.get('email', '').lower()",
        "        if User.objects.filter(email__iexact=email).exists():",
        "            raise ValidationError('This email is already registered.')",
        "        return email",
        "",
        "    def clean_username(self):",
        "        username = self.cleaned_data.get('username', '')",
        "        if len(username) < 3:",
        "            raise ValidationError('Username must be at least 3 characters.')",
        "        return username",
        "",
        "    def clean(self):",
        "        cleaned = super().clean()",
        "        pw1 = cleaned.get('password1', '')",
        "        pw2 = cleaned.get('password2', '')",
        "        if pw1 and len(pw1) < 8:",
        "            self.add_error('password1', 'Password must be at least 8 characters.')",
        "        if pw1 and pw2 and pw1 != pw2:",
        "            self.add_error('password2', 'Passwords do not match.')",
        "        return cleaned",
        "",
        "",
        "class ProfileForm(forms.ModelForm):",
        "    class Meta:",
        "        model = User",
        "        fields = ('first_name', 'last_name', 'email', 'role')",
        "",
        "    def clean_email(self):",
        "        email = self.cleaned_data.get('email', '').lower()",
        "        if User.objects.filter(email__iexact=email).exclude(pk=self.instance.pk).exists():",
        "            raise ValidationError('This email is already in use.')",
        "        return email",
        "",
        "",
    ]
    for item in report:
        m = item["model"]
        fl += [
            f"class {m}Form(forms.ModelForm):",
            "    class Meta:",
            f"        model = {m}",
            "        fields = '__all__'",
            "        widgets = {",
        ]
        for f in item["fields"]:
            if f["type"] == "TextField":
                fl.append(f"            '{f['name']}': forms.Textarea(attrs={{'rows': 3, 'maxlength': 5000}}),")
            elif f["type"] == "DateField":
                fl.append(f"            '{f['name']}': forms.DateInput(attrs={{'type': 'date'}}),")
            else:
                fl.append(f"            '{f['name']}': forms.TextInput(attrs={{'maxlength': 255}}),")
        fl += [
            "        }",
            "",
            "    def clean(self):",
            "        cleaned = super().clean()",
            "        errors = {}",
        ]
        for f in item["fields"]:
            if f["type"] == "text" or f["type"] == "CharField":
                fl.append(f"        if cleaned.get('{f['name']}', '') and len(str(cleaned['{f['name']}'])) > 255:")
                fl.append(f"            errors['{f['name']}'] = 'Maximum 255 characters.'")
        fl += [
            "        if errors: raise ValidationError(errors)",
            "        return cleaned",
            "", "",
        ]
    put(root, f"{A}/forms.py", "\n".join(fl))
