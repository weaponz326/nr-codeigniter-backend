# Generated by Django 3.2.4 on 2021-06-18 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_bills', '0002_auto_20210324_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='general',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]