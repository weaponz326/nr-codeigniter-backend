# Generated by Django 3.0.6 on 2021-03-21 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_admin', '0004_auto_20210321_0608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='access',
            old_name='customers_access',
            new_name='admissions_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='deliveries_access',
            new_name='appointments_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='menu_access',
            new_name='diagnosis_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='orders_access',
            new_name='dispensary_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='reservations_access',
            new_name='doctors_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='sittings_access',
            new_name='drugs_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='stock_access',
            new_name='laboratory_access',
        ),
        migrations.RenameField(
            model_name='access',
            old_name='tables_access',
            new_name='nurses_access',
        ),
        migrations.AddField(
            model_name='access',
            name='patients_access',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='access',
            name='prescriptions_access',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='access',
            name='wards_access',
            field=models.BooleanField(default=False),
        ),
    ]