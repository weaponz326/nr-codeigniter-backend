# Generated by Django 3.0.6 on 2021-06-13 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_patients', '0007_patient_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='photo',
            field=models.FileField(null=True, upload_to='files/patients'),
        ),
    ]
