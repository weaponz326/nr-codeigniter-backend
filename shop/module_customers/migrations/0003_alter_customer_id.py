# Generated by Django 3.2.4 on 2021-06-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_customers', '0002_customer_customer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
