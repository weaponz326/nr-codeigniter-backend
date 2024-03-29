# Generated by Django 3.0.6 on 2021-04-10 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(blank=True, max_length=20)),
                ('product_name', models.CharField(blank=True, max_length=100)),
                ('description', models.DateField(blank=True)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('price', models.CharField(blank=True, max_length=15)),
                ('stock', models.CharField(blank=True, max_length=20)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
    ]
