# Generated by Django 3.2.4 on 2021-08-23 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_admin', '0008_auto_20210823_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_level',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
