# Generated by Django 3.2.4 on 2021-07-09 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_attendance', '0006_auto_20210709_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancecheck',
            name='day',
            field=models.DateField(blank=True, null=True),
        ),
    ]
