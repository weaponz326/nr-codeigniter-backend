# Generated by Django 3.0.6 on 2021-04-07 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_code', models.CharField(blank=True, max_length=20)),
                ('booking_date', models.DateField(blank=True)),
                ('guest_name', models.CharField(blank=True, max_length=100)),
                ('expected_arrival', models.DateTimeField(blank=True)),
                ('booking_status', models.CharField(blank=True, max_length=20)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
    ]
