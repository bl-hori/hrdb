from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from employee.models import Employee

from .models import Department, Relation


class DepartmentListView(ListView):
    template_name = "department/list.html"
    context_object_name = "department_list"
    queryset = Department.objects.all()


class DepartmentDetailView(DetailView):
    template_name = "department/detail.html"
    model = Department
    context_object_name = "department"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        department = get_object_or_404(Department, id=self.kwargs.get('pk', ''))
        ctx['department'] = department

        employee_code_list = Relation.objects.filter(department_code=department.code).values_list('employee_code', flat=True)

        employee_list = []
        for code in employee_code_list:
            employee = Employee.objects.get(code=code)
            employee_list.append(employee)
        ctx['employee_list'] = employee_list

        ctx['img'] =  ["elliot", "helen", "jenny", "veronika", "stevie", "steve"]


        return ctx
