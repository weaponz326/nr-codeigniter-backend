# Generated by Django 3.0.6 on 2021-04-26 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_wards', '0002_auto_20210324_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wardpatient',
            name='date_admitted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wardpatient',
            name='date_discharged',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]