# Generated by Django 3.0.6 on 2021-03-21 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module_diagnosis', '0002_auto_20210123_0434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diagnosis',
            old_name='hospital',
            new_name='account',
        ),
    ]
