# Generated by Django 3.0.6 on 2021-06-15 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module_classes', '0003_auto_20210505_0552'),
        ('module_assessment', '0002_auto_20210503_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='clas',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='module_classes.Class'),
        ),
    ]
