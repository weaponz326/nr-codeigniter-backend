# Generated by Django 3.0.6 on 2021-06-04 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_orders', '0002_auto_20210604_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
