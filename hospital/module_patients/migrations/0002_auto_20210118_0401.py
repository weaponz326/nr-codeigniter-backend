# Generated by Django 3.0.6 on 2021-01-18 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20, null=True),
        ),
    ]