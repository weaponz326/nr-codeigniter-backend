# Generated by Django 3.0.6 on 2021-06-02 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_payables', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payable',
            name='date_paid',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payable',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='payable',
            name='payable_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
