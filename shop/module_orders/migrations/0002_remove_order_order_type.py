# Generated by Django 3.0.6 on 2021-06-02 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module_orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_type',
        ),
    ]
