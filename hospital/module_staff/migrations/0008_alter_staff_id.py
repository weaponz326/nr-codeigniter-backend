# Generated by Django 3.2.4 on 2021-06-18 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_staff', '0007_auto_20210613_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]