# Generated by Django 3.0.6 on 2021-06-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_workers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='photo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]