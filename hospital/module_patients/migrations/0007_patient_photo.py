# Generated by Django 3.0.6 on 2021-04-20 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_patients', '0006_auto_20210321_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='photo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]