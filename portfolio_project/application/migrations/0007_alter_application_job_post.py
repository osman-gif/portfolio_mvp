# Generated by Django 5.1 on 2024-09-20 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_alter_application_instructor'),
        ('posts', '0005_alter_jobpost_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='job_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.jobpost'),
        ),
    ]
