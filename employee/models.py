from django.db import models


class Employee(models.Model):
    class Meta:
        verbose_name = '従業員'
        verbose_name_plural = '従業員'

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
    name_sei_kana = models.CharField(
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
    name_mei_kana = models.CharField(
        "名_カタカナ",
        max_length=255,
        null=True,
        blank=False,
    )

    @property
    def name(self):
        return f'{self.name_sei} {self.name_mei}'

    @property
    def name_hira(self):
        return f'{self.name_sei_hira} {self.name_mei_hira}'

    @property
    def name_kata(self):
        return f'{self.name_sei_kana} {self.name_mei_kana}'

    def __str__(self):
        return f'{self.code} {self.email}'
