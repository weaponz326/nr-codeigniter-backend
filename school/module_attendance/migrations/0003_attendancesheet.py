# Generated by Django 3.2.4 on 2021-07-07 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module_students', '0006_student_clas'),
        ('module_attendance', '0002_auto_20210707_0403'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checks', models.JSONField()),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_attendance.attendance')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_students.student')),
            ],
        ),
    ]