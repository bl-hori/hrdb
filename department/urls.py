from django.urls import path

name = "Department"

from .views import DepartmentDetailView, DepartmentListView

urlpatterns = [
    path("list.html", DepartmentListView.as_view(), name="department.list"),
    path("<int:pk>/detail.html", DepartmentDetailView.as_view(), name="department.detail"),
]
