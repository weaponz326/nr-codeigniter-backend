# Generated by Django 3.2.4 on 2021-07-08 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module_ledger', '0002_auto_20210618_2004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ledgeritem',
            old_name='amount',
            new_name='credit',
        ),
        migrations.RenameField(
            model_name='ledgeritem',
            old_name='item_type',
            new_name='debit',
        ),
        migrations.RenameField(
            model_name='ledgeritem',
            old_name='details',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='ledgeritem',
            old_name='reference',
            new_name='reference_number',
        ),
    ]