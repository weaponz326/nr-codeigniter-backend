# Generated by Django 3.0.6 on 2021-05-24 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=100, null=True)),
                ('account_number', models.CharField(max_length=50, null=True)),
                ('bank_name', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('transaction_type', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_accounts.Account')),
            ],
        ),
    ]
