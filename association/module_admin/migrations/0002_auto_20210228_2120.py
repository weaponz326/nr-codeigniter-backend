# Generated by Django 3.0.6 on 2021-02-28 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module_admin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='account',
            new_name='restaurant',
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('activity_module', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_admin.User')),
            ],
        ),
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_access', models.BooleanField(default=False)),
                ('admissions_access', models.BooleanField(default=False)),
                ('appointments_access', models.BooleanField(default=False)),
                ('bills_access', models.BooleanField(default=False)),
                ('diagnosis_access', models.BooleanField(default=False)),
                ('dispensary_access', models.BooleanField(default=False)),
                ('doctors_access', models.BooleanField(default=False)),
                ('drugs_access', models.BooleanField(default=False)),
                ('laboratory_access', models.BooleanField(default=False)),
                ('nurses_access', models.BooleanField(default=False)),
                ('patients_access', models.BooleanField(default=False)),
                ('payments_access', models.BooleanField(default=False)),
                ('portal_access', models.BooleanField(default=False)),
                ('prescriptions_access', models.BooleanField(default=False)),
                ('settings_access', models.BooleanField(default=False)),
                ('staff_access', models.BooleanField(default=False)),
                ('wards_access', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_admin.User')),
            ],
        ),
    ]
