# Generated by Django 3.2.4 on 2021-06-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_assets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
