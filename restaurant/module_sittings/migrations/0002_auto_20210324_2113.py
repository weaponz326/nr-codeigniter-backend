# Generated by Django 3.0.6 on 2021-03-24 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module_sittings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitting',
            old_name='restaurant',
            new_name='account',
        ),
    ]
