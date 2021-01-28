# Generated by Django 3.0.6 on 2021-01-19 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_patients', '0002_auto_20210118_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='clinical_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='insurance_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='insurance_type',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='nationality',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='occupation',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='patient',
            name='post_code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='patient',
            name='religion',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20),
        ),
        migrations.AlterField(
            model_name='patient',
            name='state',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
