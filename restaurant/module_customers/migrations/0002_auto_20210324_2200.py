# Generated by Django 3.0.6 on 2021-03-24 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module_customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='restaurant',
            new_name='account',
        ),
    ]
