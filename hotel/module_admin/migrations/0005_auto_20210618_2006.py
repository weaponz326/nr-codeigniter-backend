# Generated by Django 3.2.4 on 2021-06-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_admin', '0004_auto_20210405_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
