# Generated by Django 3.2.4 on 2021-07-09 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_appraisal', '0005_auto_20210709_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appraisalform',
            name='attendace',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='appraisalform',
            name='dependability',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='appraisalform',
            name='knowledge',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='appraisalform',
            name='productivity',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='appraisalform',
            name='rating',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='appraisalform',
            name='relations',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='appraisalform',
            name='work_quality',
            field=models.NullBooleanField(),
        ),
    ]
