"""Generate role-based permissions module."""
from helpers import put

def generate_permissions(report, root, A):
    put(root, f"{A}/permissions.py", CODE)
    print("  Permissions: role decorators + DRF classes")

CODE = r'''from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
from rest_framework.permissions import BasePermission

# --- Role check helpers ---
def _is_admin(user):
    return user.is_authenticated and (user.role == "admin" or user.is_superuser)

def _is_creator(user):
    return user.is_authenticated and user.role in ("creator", "admin")

# --- View decorators ---
def admin_required(view):
    @wraps(view)
    def wrapper(request, *a, **kw):
        if not request.user.is_authenticated:
            return redirect("login")
        if not _is_admin(request.user):
            messages.error(request, "Admin access required.")
            return redirect("dashboard")
        return view(request, *a, **kw)
    return wrapper

def creator_required(view):
    @wraps(view)
    def wrapper(request, *a, **kw):
        if not request.user.is_authenticated:
            return redirect("login")
        if not _is_creator(request.user):
            messages.error(request, "Creator access required.")
            return redirect("dashboard")
        return view(request, *a, **kw)
    return wrapper

def login_required_page(view):
    @wraps(view)
    def wrapper(request, *a, **kw):
        if not request.user.is_authenticated:
            return redirect("login")
        return view(request, *a, **kw)
    return wrapper

# --- DRF Permission Classes ---
class IsAdminRole(BasePermission):
    def has_permission(self, request, view):
        return request.user and _is_admin(request.user)

class IsCreatorRole(BasePermission):
    def has_permission(self, request, view):
        return request.user and _is_creator(request.user)

class IsSelfOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return _is_admin(request.user) or getattr(obj, "user_id", getattr(obj, "id", None)) == request.user.id

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in ("GET", "HEAD", "OPTIONS")

class CanWrite(BasePermission):
    """Read for all, write only for admin or creator."""
    def has_permission(self, request, view):
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True
        return request.user and _is_creator(request.user)
'''
