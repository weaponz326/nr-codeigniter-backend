# Generated by Django 3.2.4 on 2021-07-07 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_payroll', '0006_alter_payroll_date_generated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='date_generated',
            field=models.DateField(blank=True, null=True),
        ),
    ]
