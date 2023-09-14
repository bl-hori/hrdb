from functools import reduce
from operator import and_

from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView

from employee.models import Employee


class EmployeeListView(ListView):
    template_name = "employee/list.html"
    context_object_name = "employee_list"
    queryset = Employee.objects.all()


class EmployeeSearchView(TemplateView):
    template_name = "employee/search.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        parameters = self.request.GET
        groups = []
        objects = Employee.objects.filter()

        if parameters.get('q', None):
            params = self.parse_search_params(parameters.get('q'))
            ctx['q'] = " ".join(params)

            query = reduce(
                and_,
                [
                    Q(code__icontains=p)
                    | Q(email__icontains=p)
                    | Q(name_sei__icontains=p)
                    | Q(name_mei__icontains=p)
                    | Q(name_sei_kana__icontains=p)
                    | Q(name_mei_kana__icontains=p)
                    | Q(name_sei_hira__icontains=p)
                    | Q(name_mei_hira__icontains=p)
                    for p in params
                ],
            )
            objects = objects.filter(query)

        order = parameters.get('order', None)

        if order:
            ctx['order'] = order

        if order == 'gender':
            objects_filter = objects.filter(detail__e_gender="男性")
            group = {
                'header' : f'男性 ({len(objects_filter)}名)',
                'table' : objects_filter,
            }
            groups.append(group)

            objects_filter = objects.filter(detail__e_gender="女性")
            group = {
                'header' : f'女性 ({len(objects_filter)}名)',
                'table' : objects_filter,
            }
            groups.append(group)
        else:
            table = objects.all()
            group = {
                'header' : f'全体 ({len(table)}名)',
                'table' : table,
            }
            groups.append(group)

        ctx['employee_list_groups'] = groups

        return ctx

    def parse_search_params(self, words: str) -> list:
        seach_words = words.replace("　", " ").split()
        return seach_words


class EmployeeDetailView(DetailView):
    template_name = "employee/detail.html"
    model = Employee
    context_object_name = "employee"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['employee'] = get_object_or_404(Employee, id=self.kwargs.get('pk', ''))
        ctx['img'] =  ["elliot", "helen", "jenny", "veronika", "stevie", "steve"]
        return ctx
