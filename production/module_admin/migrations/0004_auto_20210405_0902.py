# Generated by Django 3.0.6 on 2021-04-05 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module_admin', '0003_auto_20210324_1919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='access',
            old_name='admissions_access',
            new_name='contractors_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='appointments_access',
            new_name='equipment_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='bills_access',
            new_name='manufacturing_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='diagnosis_access',
            new_name='orders_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='dispensary_access',
            new_name='products_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='doctors_access',
            new_name='projects_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='drugs_access',
            new_name='purchasing_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='laboratory_access',
            new_name='schedule_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='nurses_access',
            new_name='stock_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='patients_access',
            new_name='tasks_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='payments_access',
            new_name='workers_access',
        ),
        migrations.RemoveField(
            model_name='access',
            name='prescriptions_access',
        ),
        migrations.RemoveField(
            model_name='access',
            name='staff_access',
        ),
        migrations.RemoveField(
            model_name='access',
            name='wards_access',
        ),
    ]
