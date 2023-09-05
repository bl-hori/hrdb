from functools import reduce
from operator import and_

from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Department


class DepartmentListView(ListView):
    template_name = "department/list.html"
    context_object_name = "department_list"
    queryset = Department.objects.all()