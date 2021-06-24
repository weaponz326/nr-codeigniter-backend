# Generated by Django 3.2.4 on 2021-06-22 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module_wards', '0004_auto_20210618_1956'),
        ('module_dispensary', '0004_auto_20210618_1956'),
        ('module_appointments', '0007_alter_appointment_id'),
        ('module_laboratory', '0006_auto_20210618_1956'),
        ('module_bills', '0004_appointmentcharge_dispensarycharge_laboratorycharge_wardcharge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmentcharge',
            name='item',
        ),
        migrations.RemoveField(
            model_name='dispensarycharge',
            name='item',
        ),
        migrations.RemoveField(
            model_name='laboratorycharge',
            name='item',
        ),
        migrations.RemoveField(
            model_name='wardcharge',
            name='item',
        ),
        migrations.AddField(
            model_name='appointmentcharge',
            name='appointment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='module_appointments.appointment'),
        ),
        migrations.AddField(
            model_name='dispensarycharge',
            name='dispensary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='module_dispensary.dispensary'),
        ),
        migrations.AddField(
            model_name='laboratorycharge',
            name='lab',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='module_laboratory.laboratory'),
        ),
        migrations.AddField(
            model_name='wardcharge',
            name='ward',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='module_wards.ward'),
        ),
    ]
