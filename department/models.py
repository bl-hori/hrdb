from django.db import models


class Department(models.Model):
    class Meta:
        verbose_name = '組織'
        verbose_name_plural = '組織'

    code = models.CharField(
        "組織番号",
        max_length=255,
        null=True,
        blank=False,
        unique=True,
    )

    dept_code = models.CharField(
        "組織整列番号",
        max_length=255,
        null=True,
        blank=False,
        unique=True,
    )

    dept_parent_code = models.CharField(
        "親組織整列番号",
        max_length=255,
        null=True,
        blank=False,
    )

    path = models.CharField(
        "組織系列",
        max_length=255,
        null=True,
        blank=False,
        unique=True,
    )

    name = models.CharField(
        "組織名",
        max_length=255,
        null=True,
        blank=False,
        unique=True,
    )

    def __str__(self):
        return f'{self.dept_code} {self.path}'
