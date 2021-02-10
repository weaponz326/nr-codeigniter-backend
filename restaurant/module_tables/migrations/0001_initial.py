# Generated by Django 3.0.6 on 2021-02-02 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.CharField(blank=True, max_length=20)),
                ('table_type', models.CharField(blank=True, max_length=50)),
                ('capacity', models.CharField(blank=True, max_length=9)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('table_status', models.CharField(blank=True, max_length=50)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
    ]