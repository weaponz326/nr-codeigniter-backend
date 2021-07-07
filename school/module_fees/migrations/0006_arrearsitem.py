# Generated by Django 3.2.4 on 2021-07-04 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module_fees', '0005_targetclass'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArrearsItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=100)),
                ('fee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fee', to='module_fees.fee')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='module_fees.fee')),
            ],
        ),
    ]
