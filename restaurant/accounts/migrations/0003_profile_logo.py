# Generated by Django 3.2.4 on 2021-08-18 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='logo',
            field=models.FileField(null=True, upload_to='profile'),
        ),
    ]
