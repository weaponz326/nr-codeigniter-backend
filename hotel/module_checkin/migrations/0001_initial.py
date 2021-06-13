# Generated by Django 3.0.6 on 2021-04-07 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_code', models.CharField(blank=True, max_length=20)),
                ('checkin_date', models.DateTimeField(blank=True, null=True)),
                ('checkout_date', models.DateTimeField(blank=True, null=True)),
                ('number_nights', models.CharField(blank=True, max_length=5)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
    ]