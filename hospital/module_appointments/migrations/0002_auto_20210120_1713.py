# Generated by Django 3.0.6 on 2021-01-20 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]