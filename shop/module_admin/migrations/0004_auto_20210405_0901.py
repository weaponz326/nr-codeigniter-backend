# Generated by Django 3.0.6 on 2021-04-05 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module_admin', '0003_auto_20210324_1919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='access',
            old_name='admissions_access',
            new_name='cashflow_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='appointments_access',
            new_name='customers_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='bills_access',
            new_name='inventory_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='diagnosis_access',
            new_name='invoice_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='dispensary_access',
            new_name='marketting_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='doctors_access',
            new_name='orders_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='drugs_access',
            new_name='payables_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='laboratory_access',
            new_name='products_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='nurses_access',
            new_name='purcahsing_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='patients_access',
            new_name='receivables_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='prescriptions_access',
            new_name='sales_access',
        ),
        migrations.RemoveField(
            model_name='access',
            name='wards_access',
        ),
    ]
