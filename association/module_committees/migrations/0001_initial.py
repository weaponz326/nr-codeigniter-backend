# Generated by Django 3.0.6 on 2021-05-24 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('module_members', '0002_member_member_code'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('committee_name', models.CharField(blank=True, max_length=200)),
                ('date_formed', models.DateField(null=True)),
                ('description', models.TextField(blank=True)),
                ('committee_status', models.CharField(blank=True, max_length=200)),
                ('functions', models.TextField(blank=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='CommitteeMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('committee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_committees.Committee')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_members.Member')),
            ],
        ),
    ]
