from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("base.urls")),
    path("employee/", include("employee.urls")),
    path("department/", include("department.urls")),
]
