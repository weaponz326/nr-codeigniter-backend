# Generated by Django 3.0.6 on 2021-03-21 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module_admin', '0003_auto_20210227_0549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='access',
            old_name='admissions_access',
            new_name='customers_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='appointments_access',
            new_name='deliveries_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='diagnosis_access',
            new_name='menu_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='dispensary_access',
            new_name='orders_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='doctors_access',
            new_name='reservations_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='drugs_access',
            new_name='sittings_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='laboratory_access',
            new_name='stock_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='nurses_access',
            new_name='tables_access',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='hospital',
            new_name='account',
        ),
        migrations.RemoveField(
            model_name='access',
            name='patients_access',
        ),
        migrations.RemoveField(
            model_name='access',
            name='prescriptions_access',
        ),
        migrations.RemoveField(
            model_name='access',
            name='wards_access',
        ),
    ]
