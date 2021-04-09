# Generated by Django 3.0.6 on 2021-04-05 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('sex', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=50)),
                ('religion', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('address', models.TextField(blank=True)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('post_code', models.CharField(blank=True, max_length=20)),
                ('staff_code', models.CharField(blank=True, max_length=50)),
                ('department', models.CharField(blank=True, max_length=100)),
                ('job', models.CharField(blank=True, max_length=50)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
    ]
