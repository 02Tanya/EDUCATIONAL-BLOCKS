from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("edblocks/", include("edblocks.urls", namespace="edblocks")),
    path("users/", include("users.urls", namespace="users")),
]
