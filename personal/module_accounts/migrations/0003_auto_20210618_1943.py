# Generated by Django 3.2.4 on 2021-06-18 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_accounts', '0002_auto_20200813_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]