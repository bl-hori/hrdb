from django.urls import path

name = "Department"

from .views import DepartmentListView

urlpatterns = [
    path("list.html", DepartmentListView.as_view(), name="department.list"),
]
