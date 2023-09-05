from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportMixin

from . import models


class DepartmentResource(resources.ModelResource):
    class Meta:
        model = models.Department


class DepartmentAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = DepartmentResource


admin.site.register(models.Department, DepartmentAdmin)
