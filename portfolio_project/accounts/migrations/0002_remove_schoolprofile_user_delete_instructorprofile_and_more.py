# Generated by Django 5.1 on 2024-09-01 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='InstructorProfile',
        ),
        migrations.DeleteModel(
            name='SchoolProfile',
        ),
    ]
