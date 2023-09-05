from functools import reduce
from operator import and_

from django.db.models import Q
from django.views.generic import ListView

from employee.models import Employee


class EmployeeListView(ListView):
    template_name = "employee/list.html"
    context_object_name = "employee_list"
    queryset = Employee.objects.all()


class EmployeeSearchView(ListView):
    template_name = "employee/search.html"
    context_object_name = "employee_list"

    def get_context_data(self):
        ctx = super().get_context_data()
        ctx["q"] = " ".join(self.parse_search_params(self.request.GET.get("q", "")))
        return ctx

    def get_queryset(self):
        if self.request.GET.get("q", ""):
            params = self.parse_search_params(self.request.GET["q"])
            query = reduce(
                and_,
                [
                    Q(code__icontains=p)
                    | Q(email__icontains=p)
                    | Q(name_sei__icontains=p)
                    | Q(name_mei__icontains=p)
                    | Q(name_sei_kata__icontains=p)
                    | Q(name_mei_kata__icontains=p)
                    | Q(name_sei_hira__icontains=p)
                    | Q(name_mei_hira__icontains=p)
                    for p in params
                ],
            )
            return Employee.objects.filter(query)
        else:
            return None

    def parse_search_params(self, words: str) -> list:
        seach_words = words.replace("　", " ").split()
        return seach_words
