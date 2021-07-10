# Generated by Django 3.2.4 on 2021-07-10 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('module_members', '0004_alter_member_id'),
        ('accounts', '0002_alter_profile_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dues_code', models.CharField(blank=True, max_length=20)),
                ('dues_name', models.CharField(blank=True, max_length=100)),
                ('dues_date', models.DateField(blank=True, null=True)),
                ('amount', models.CharField(blank=True, max_length=15)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='DuesPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('amount', models.CharField(blank=True, max_length=15)),
                ('dues', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_dues.dues')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_members.member')),
            ],
        ),
    ]
