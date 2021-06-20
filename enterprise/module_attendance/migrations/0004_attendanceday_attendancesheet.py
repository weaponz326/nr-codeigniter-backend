# Generated by Django 3.2.4 on 2021-06-19 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module_employees', '0006_alter_employee_id'),
        ('module_attendance', '0003_auto_20210619_0244'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checks', models.JSONField()),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_attendance.attendance')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_employees.employee')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(blank=True, null=True)),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_attendance.attendance')),
            ],
        ),
    ]