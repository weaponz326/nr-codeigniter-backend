# Generated by Django 3.0.6 on 2021-03-24 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_sittings', '0002_auto_20210324_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitting',
            name='customer_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='number_guests',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sitting',
            name='sitting_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
