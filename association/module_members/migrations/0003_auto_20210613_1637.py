# Generated by Django 3.0.6 on 2021-06-13 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_members', '0002_member_member_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.FileField(null=True, upload_to='members'),
        ),
    ]
