# Generated by Django 3.0.6 on 2021-04-12 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('module_suppliers', '0001_initial'),
        ('accounts', '0001_initial'),
        ('module_products', '0002_auto_20210410_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchasing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchasing_number', models.CharField(blank=True, max_length=20)),
                ('purchasing_date', models.DateField(blank=True, null=True)),
                ('supplier_invoice', models.CharField(blank=True, max_length=30)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_suppliers.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='PurchasingItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(blank=True, max_length=20)),
                ('total_price', models.CharField(blank=True, max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_products.Product')),
                ('purchasing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_purchasing.Purchasing')),
            ],
        ),
    ]