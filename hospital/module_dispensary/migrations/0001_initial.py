# Generated by Django 3.0.6 on 2021-01-25 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('module_prescriptions', '0001_initial'),
        ('accounts', '0001_initial'),
        ('module_drugs', '0003_auto_20210124_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispensary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispense_code', models.CharField(blank=True, max_length=50)),
                ('dispense_date', models.DateField(blank=True, null=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
                ('prescription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='module_prescriptions.Prescription')),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.TextField(blank=True)),
                ('dispensary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_dispensary.Dispensary')),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_drugs.Drug')),
            ],
        ),
    ]
