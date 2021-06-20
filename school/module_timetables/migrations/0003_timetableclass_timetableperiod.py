# Generated by Django 3.2.4 on 2021-06-18 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module_timetables', '0002_timetable_term'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimetablePeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(blank=True, max_length=100)),
                ('period_start', models.TimeField(blank=True, null=True)),
                ('period_end', models.TimeField(blank=True, null=True)),
                ('timetable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_timetables.timetable')),
            ],
        ),
        migrations.CreateModel(
            name='TimetableClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clas', models.CharField(blank=True, max_length=100)),
                ('timetable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_timetables.timetable')),
            ],
        ),
    ]
