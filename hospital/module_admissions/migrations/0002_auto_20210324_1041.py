# Generated by Django 3.0.6 on 2021-03-24 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module_admissions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admission',
            old_name='hospital',
            new_name='account',
        ),
    ]