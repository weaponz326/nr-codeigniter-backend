# Generated by Django 3.2.4 on 2021-06-18 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_deliveries', '0002_auto_20210324_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
