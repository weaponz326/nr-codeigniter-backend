# Generated by Django 3.0.6 on 2021-05-05 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='photo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
