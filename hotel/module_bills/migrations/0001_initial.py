# Generated by Django 3.0.6 on 2021-04-09 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('module_guests', '0001_initial'),
        ('module_services', '0001_initial'),
        ('module_rooms', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_code', models.CharField(blank=True, max_length=20)),
                ('bill_date', models.DateField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_guests.Guest')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(blank=True, max_length=20)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_bills.Bill')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_services.Service')),
            ],
        ),
        migrations.CreateModel(
            name='RoomBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_nights', models.CharField(blank=True, max_length=20)),
                ('amount', models.CharField(blank=True, max_length=20)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_bills.Bill')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_rooms.Room')),
            ],
        ),
    ]