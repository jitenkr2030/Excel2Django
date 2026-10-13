"""Generate serializers.py and api.py with role permissions + filters."""
from helpers import put

def generate_serializers(report, root, A):
    names = [i["model"] for i in report]
    mi = "from .models import User" + (", " + ", ".join(names) if names else "")
    lines = [
        "from rest_framework import serializers",
        mi,
        "",
        "",
        "class UserSerializer(serializers.ModelSerializer):",
        "    password = serializers.CharField(write_only=True, required=False)",
        "    class Meta:",
        "        model = User",
        "        fields = ('id','username','email','first_name','last_name','role','is_active','is_staff','date_joined','password')",
        "        read_only_fields = ('id','date_joined')",
        "    def create(self, validated_data):",
        "        pw = validated_data.pop('password', None)",
        "        user = User(**validated_data)",
        "        if pw: user.set_password(pw)",
        "        user.save()",
        "        return user",
        "    def update(self, instance, validated_data):",
        "        pw = validated_data.pop('password', None)",
        "        for k,v in validated_data.items(): setattr(instance,k,v)",
        "        if pw: instance.set_password(pw)",
        "        instance.save()",
        "        return instance",
        "",
        "",
        "class RegisterSerializer(serializers.ModelSerializer):",
        "    password = serializers.CharField(write_only=True, min_length=8)",
        "    class Meta:",
        "        model = User",
        "        fields = ('username','email','first_name','last_name','role','password')",
        "    def validate_email(self, value):",
        "        if User.objects.filter(email=value).exists():",
        "            raise serializers.ValidationError('Email already registered.')",
        "        return value",
        "    def validate_username(self, value):",
        "        if User.objects.filter(username=value).exists():",
        "            raise serializers.ValidationError('Username already taken.')",
        "        return value",
        "    def create(self, validated_data):",
        "        return User.objects.create_user(**validated_data)",
        "",
        "",
    ]
    for n in names:
        lines += [
            f"class {n}Serializer(serializers.ModelSerializer):",
            "    class Meta:",
            f"        model = {n}",
            "        fields = '__all__'",
            "",
            "",
        ]
    put(root, f"{A}/serializers.py", "\n".join(lines))

def generate_api(report, root, A, title):
    names = [i["model"] for i in report]
    si = "from .serializers import UserSerializer, RegisterSerializer"
    if names:
        si += ", " + ", ".join(f"{n}Serializer" for n in names)
    mi = "from .models import User"
    if names:
        mi += ", " + ", ".join(names)
    pi = "from .permissions import IsAdminRole, IsCreatorRole, CanWrite, ReadOnly"
    lines = [
        "from rest_framework import viewsets, status, permissions, filters as drf_filters",
        "from rest_framework.decorators import api_view, permission_classes, action",
        "from rest_framework.response import Response",
        "from rest_framework.routers import DefaultRouter",
        "from rest_framework.pagination import PageNumberPagination",
        "from django.urls import path",
        mi,
        si,
        pi,
        "",
        "",
        "class StandardPagination(PageNumberPagination):",
        "    page_size = 25",
        "    page_size_query_param = 'page_size'",
        "    max_page_size = 100",
        "",
        "",
        "class UserViewSet(viewsets.ModelViewSet):",
        "    queryset = User.objects.all()",
        "    serializer_class = UserSerializer",
        "    pagination_class = StandardPagination",
        "    filter_backends = [drf_filters.SearchFilter, drf_filters.OrderingFilter]",
        "    search_fields = ('username','email','first_name','last_name','role')",
        "    ordering_fields = ('id','username','email','role','date_joined')",
        "    ordering = ['-id']",
        "    permission_classes = [permissions.IsAuthenticated]",
        "    def get_permissions(self):",
        "        if self.action in ('list','retrieve'):",
        "            return [permissions.IsAuthenticated()]",
        "        return [IsAdminRole()]",
        "",
        "",
        "@api_view(['POST'])",
        "@permission_classes([permissions.AllowAny])",
        "def register_api(request):",
        "    s = RegisterSerializer(data=request.data)",
        "    if s.is_valid():",
        "        s.save()",
        "        return Response(s.data, status=status.HTTP_201_CREATED)",
        "    return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)",
        "",
        "",
    ]
    for n in names:
        fn = [f["name"] for f in item.get("fields", [])[:5]] if "item" in dir() else []
        sf = ", ".join(f"'{f}'" for f in ["id"] + [x for x in fn[:3]])
        lines += [
            f"class {n}ViewSet(viewsets.ModelViewSet):",
            f"    queryset = {n}.objects.all()",
            f"    serializer_class = {n}Serializer",
            "    pagination_class = StandardPagination",
            "    filter_backends = [drf_filters.SearchFilter, drf_filters.OrderingFilter]",
            f"    search_fields = ('id',)",
            "    ordering_fields = ('id',)",
            "    ordering = ['-id']",
            "    def get_permissions(self):",
            "        if self.action in ('list','retrieve'):",
            "            return [permissions.IsAuthenticated()]",
            "        return [CanWrite()]",
            "",
            "",
        ]
    # Fix search_fields with actual fields
    lines_fixed = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("search_fields = ('id',)"):
            # Find which model we're in
            for j in range(i-1, max(0, i-5), -1):
                if "ViewSet" in lines[j] and "class" in lines[j]:
                    model_name = lines[j].replace("class ","").replace("ViewSet(viewsets.ModelViewSet):","")
                    # Find fields in report
                    for item in report:
                        if item["model"] == model_name:
                            fn = [f["name"] for f in item["fields"][:5]]
                            sf = ", ".join(f"'{x}'" for x in fn[:3])
                            lines[i] = f"    search_fields = ({sf})"
                            of = ", ".join(f"'{x}'" for x in (['id'] + fn[:4]))
                            lines[i+1] = f"    ordering_fields = ({of})"
                            break
                    break
        lines_fixed.append(line)
        i += 1
    lines = lines_fixed

    lines += [
        "router = DefaultRouter()",
        "router.register(r'users', UserViewSet)",
    ]
    for n in names:
        lines.append(f"router.register(r'{n.lower()}', {n}ViewSet)")
    lines += [
        "",
        "register_url = path('register/', register_api)",
    ]
    put(root, f"{A}/api.py", "\n".join(lines))
