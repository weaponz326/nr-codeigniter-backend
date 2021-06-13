# Generated by Django 3.0.6 on 2021-04-11 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('module_products', '0002_auto_20210410_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=50)),
                ('container', models.CharField(blank=True, max_length=50)),
                ('bin_number', models.CharField(blank=True, max_length=50)),
                ('quantity', models.CharField(blank=True, max_length=30)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_products.Product')),
            ],
        ),
    ]