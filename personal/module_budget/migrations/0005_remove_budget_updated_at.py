# Generated by Django 3.0.6 on 2020-09-29 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module_budget', '0004_auto_20200813_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='updated_at',
        ),
    ]