# Generated by Django 5.1 on 2024-09-21 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_remove_schoolprofile_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
