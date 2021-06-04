# Generated by Django 3.0.6 on 2021-06-03 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module_products', '0002_auto_20210410_1200'),
        ('module_suppliers', '0002_supplierproduct'),
        ('module_purchasing', '0002_remove_purchasing_supplier_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasing',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='module_suppliers.Supplier'),
        ),
        migrations.AlterField(
            model_name='purchasingitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='module_products.Product'),
        ),
    ]
