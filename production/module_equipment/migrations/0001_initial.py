# Generated by Django 3.0.6 on 2021-04-14 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_code', models.CharField(blank=True, max_length=20)),
                ('equipment_name', models.CharField(blank=True, max_length=100)),
                ('equipment_type', models.CharField(blank=True, max_length=100)),
                ('category', models.CharField(blank=True, max_length=50)),
                ('brand', models.CharField(blank=True, max_length=50)),
                ('model', models.CharField(blank=True, max_length=50)),
                ('serial_number', models.CharField(blank=True, max_length=30)),
                ('description', models.TextField(blank=True)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('condition', models.CharField(blank=True, max_length=50)),
                ('equipment_status', models.CharField(blank=True, max_length=50)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
    ]