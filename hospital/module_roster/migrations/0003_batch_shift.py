# Generated by Django 3.2.4 on 2021-06-24 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module_roster', '0002_alter_roster_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_name', models.CharField(blank=True, max_length=100)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('roster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_roster.roster')),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(blank=True, max_length=100)),
                ('batch_symbol', models.CharField(blank=True, max_length=20)),
                ('roster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_roster.roster')),
            ],
        ),
    ]
