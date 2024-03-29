# Generated by Django 3.0.6 on 2021-04-03 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledger_name', models.CharField(blank=True, max_length=100)),
                ('ledger_code', models.CharField(blank=True, max_length=20)),
                ('ledger_date', models.DateField(blank=True, null=True)),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='LedgerItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_date', models.DateField(blank=True, null=True)),
                ('reference', models.CharField(blank=True, max_length=20)),
                ('details', models.TextField(null=True)),
                ('item_type', models.CharField(blank=True, max_length=20)),
                ('amount', models.CharField(blank=True, max_length=20)),
                ('balance', models.CharField(blank=True, max_length=20)),
                ('ledger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_ledger.Ledger')),
            ],
        ),
    ]
