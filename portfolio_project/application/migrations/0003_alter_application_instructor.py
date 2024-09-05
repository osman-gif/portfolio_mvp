# Generated by Django 5.1 on 2024-09-02 12:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_alter_application_instructor'),
        ('instructor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructor.instructorprofile'),
        ),
    ]
