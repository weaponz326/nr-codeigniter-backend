# Generated by Django 3.2.4 on 2021-07-05 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module_terms', '0002_alter_term_id'),
        ('module_classes', '0005_auto_20210705_0531'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='term',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='module_terms.term'),
        ),
        migrations.DeleteModel(
            name='ClassStudent',
        ),
    ]
