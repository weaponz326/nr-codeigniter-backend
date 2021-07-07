# Generated by Django 3.2.4 on 2021-07-05 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module_students', '0005_remove_student_clas'),
        ('module_classes', '0004_auto_20210618_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='term',
        ),
        migrations.CreateModel(
            name='ClassStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_classes.class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='module_students.student')),
            ],
        ),
    ]
