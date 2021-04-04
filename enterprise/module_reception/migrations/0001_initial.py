# Generated by Django 3.0.6 on 2021-04-04 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_code', models.CharField(blank=True, max_length=20)),
                ('visit_date', models.DateField(blank=True, null=True)),
                ('visitor_name', models.CharField(blank=True, max_length=100)),
                ('visitor_phone', models.CharField(blank=True, max_length=20)),
                ('arrival', models.TimeField(blank=True, null=True)),
                ('departure', models.TimeField(blank=True, null=True)),
                ('purpose', models.CharField(blank=True, max_length=100)),
                ('tag_number', models.CharField(blank=True, max_length=20)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
    ]
