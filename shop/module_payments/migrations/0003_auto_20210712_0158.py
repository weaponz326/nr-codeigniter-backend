# Generated by Django 3.2.4 on 2021-07-12 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module_payments', '0002_alter_payment_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='amount_paid',
            new_name='payment',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='balance',
        ),
    ]
