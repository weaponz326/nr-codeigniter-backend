# Generated by Django 3.2.4 on 2021-07-11 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module_bookings', '0002_alter_booking_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookedRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(blank=True, max_length=100)),
                ('persons_number', models.CharField(blank=True, max_length=10)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_bookings.booking')),
            ],
        ),
    ]
