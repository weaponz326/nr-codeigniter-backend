# Generated by Django 3.0.6 on 2021-06-13 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module_customers', '0003_customer_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='photo',
        ),
    ]
