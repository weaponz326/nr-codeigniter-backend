# Generated by Django 3.0.6 on 2021-06-13 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_staff', '0006_staff_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='photo',
            field=models.FileField(null=True, upload_to='staff'),
        ),
    ]
