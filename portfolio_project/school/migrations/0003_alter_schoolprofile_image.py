# Generated by Django 5.1 on 2024-09-20 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_schoolprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
