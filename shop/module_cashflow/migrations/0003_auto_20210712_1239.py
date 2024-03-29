# Generated by Django 3.2.4 on 2021-07-12 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_id'),
        ('module_cashflow', '0002_alter_sheet_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='cashflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet_code', models.CharField(blank=True, max_length=20)),
                ('sheet_name', models.CharField(blank=True, max_length=100)),
                ('sheet_type', models.CharField(blank=True, max_length=30)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
        migrations.DeleteModel(
            name='Sheet',
        ),
    ]
