from django.urls import path

from employee.views import EmployeeDetailView, EmployeeListView, EmployeeSearchView

name = "employee"

urlpatterns = [
    path("list.html", EmployeeListView.as_view(), name="employee.list"),
    path("search.html", EmployeeSearchView.as_view(), name="employee.search"),
    path("<int:pk>/detail.html", EmployeeDetailView.as_view(), name="employee.detail"),
]
