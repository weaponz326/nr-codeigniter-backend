# Generated by Django 3.2.4 on 2021-08-20 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_admin', '0006_auto_20210820_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='invitation_status',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
