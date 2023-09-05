from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportMixin

from . import models


class EmployeeResource(resources.ModelResource):
    class Meta:
        model = models.Employee


class EmployeeAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = EmployeeResource


admin.site.register(models.Employee, EmployeeAdmin)
