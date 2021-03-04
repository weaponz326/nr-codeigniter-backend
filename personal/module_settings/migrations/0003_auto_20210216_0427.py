# Generated by Django 3.0.6 on 2021-02-16 04:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('module_settings', '0002_auto_20201026_0656'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(null=True)),
                ('gender', models.CharField(max_length=20, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('address', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
        migrations.RemoveField(
            model_name='locationdetails',
            name='user',
        ),
        migrations.DeleteModel(
            name='AdditionalProfile',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='LocationDetails',
        ),
    ]
