# Generated by Django 3.0.6 on 2021-06-13 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_employees', '0004_auto_20210513_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.FileField(null=True, upload_to='employees'),
        ),
    ]
