# Generated by Django 3.2.4 on 2021-06-18 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_fees', '0003_feesitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='feesitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]