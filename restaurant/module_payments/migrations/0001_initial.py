# Generated by Django 3.2.4 on 2021-07-03 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('module_orders', '0004_order_order_total'),
        ('accounts', '0002_alter_profile_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_code', models.CharField(blank=True, max_length=50)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=11, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='module_orders.order')),
            ],
        ),
    ]
