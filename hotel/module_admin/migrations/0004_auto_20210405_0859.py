# Generated by Django 3.0.6 on 2021-04-05 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module_admin', '0003_auto_20210324_1919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='access',
            old_name='admissions_access',
            new_name='assets_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='appointments_access',
            new_name='bookings_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='diagnosis_access',
            new_name='checkin_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='dispensary_access',
            new_name='guests_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='doctors_access',
            new_name='housekeeping_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='drugs_access',
            new_name='rooms_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='laboratory_access',
            new_name='services_access',
        ),
        migrations.RemoveField(
            model_name='access',
            name='nurses_access',
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
