# Generated by Django 4.2.5 on 2023-09-13 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, null=True, unique=True, verbose_name='社員番号')),
                ('email', models.CharField(max_length=255, null=True, verbose_name='メールアドレス')),
                ('name_sei', models.CharField(max_length=255, null=True, verbose_name='姓')),
                ('name_sei_hira', models.CharField(max_length=255, null=True, verbose_name='姓_ひらがな')),
                ('name_sei_kana', models.CharField(max_length=255, null=True, verbose_name='姓_カタカナ')),
                ('name_mei', models.CharField(max_length=255, null=True, verbose_name='名')),
                ('name_mei_hira', models.CharField(max_length=255, null=True, verbose_name='名_ひらがな')),
                ('name_mei_kana', models.CharField(max_length=255, null=True, verbose_name='名_カタカナ')),
                ('department_code', models.CharField(max_length=255, null=True, verbose_name='組織番号')),
            ],
            options={
                'verbose_name': '従業員',
                'verbose_name_plural': '従業員',
            },
        ),
        migrations.CreateModel(
            name='EmployeeDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, verbose_name='社員番号')),
                ('e_gender', models.CharField(max_length=255, verbose_name='性別')),
                ('e_hiredate', models.CharField(max_length=255, verbose_name='入社日')),
                ('e_work', models.CharField(max_length=255, verbose_name='雇用形態')),
                ('e_type', models.CharField(max_length=255, verbose_name='職種')),
                ('e_post', models.CharField(max_length=255, verbose_name='役職')),
                ('e_place', models.CharField(max_length=255, verbose_name='事業所')),
                ('employee', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='employee.employee')),
            ],
            options={
                'verbose_name': '従業員詳細',
                'verbose_name_plural': '従業員詳細',
            },
        ),
    ]
