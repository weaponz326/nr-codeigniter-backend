# Generated by Django 3.0.6 on 2021-03-07 05:52

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
            new_name='school',
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
                ('assessment_access', models.BooleanField(default=False)),
                ('attendance_access', models.BooleanField(default=False)),
                ('classes_access', models.BooleanField(default=False)),
                ('fees_access', models.BooleanField(default=False)),
                ('parents_access', models.BooleanField(default=False)),
                ('payments_access', models.BooleanField(default=False)),
                ('portal_access', models.BooleanField(default=False)),
                ('reports_access', models.BooleanField(default=False)),
                ('settings_access', models.BooleanField(default=False)),
                ('staff_access', models.BooleanField(default=False)),
                ('students_access', models.BooleanField(default=False)),
                ('subjects_access', models.BooleanField(default=False)),
                ('teachers_access', models.BooleanField(default=False)),
                ('terms_access', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_admin.User')),
            ],
        ),
    ]
