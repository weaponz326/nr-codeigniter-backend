# Generated by Django 3.2.4 on 2021-06-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_invoice', '0002_auto_20210602_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]