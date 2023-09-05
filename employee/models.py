from django.db import models


class Employee(models.Model):
    code = models.CharField(
        "社員番号",
        max_length=255,
        null=True,
        blank=False,
        unique=True,
    )
    email = models.CharField(
        "メールアドレス",
        max_length=255,
        null=True,
        blank=False,
    )
    name_sei = models.CharField(
        "姓",
        max_length=255,
        null=True,
        blank=False,
    )
    name_sei_hira = models.CharField(
        "姓_ひらがな",
        max_length=255,
        null=True,
        blank=False,
    )
    name_sei_kata = models.CharField(
        "姓_カタカナ",
        max_length=255,
        null=True,
        blank=False,
    )
    name_mei = models.CharField(
        "名",
        max_length=255,
        null=True,
        blank=False,
    )
    name_mei_hira = models.CharField(
        "名_ひらがな",
        max_length=255,
        null=True,
        blank=False,
    )
    name_mei_kata = models.CharField(
        "名_カタカナ",
        max_length=255,
        null=True,
        blank=False,
    )

    def __str__(self):
        return " ".join([self.code, self.name_sei_hira, self.name_mei_hira])
