# Generated by Django 3.0.6 on 2021-05-03 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module_bills', '0002_auto_20210324_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='bill_type',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='delivery',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='sitting',
        ),
    ]