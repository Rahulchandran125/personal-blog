# Generated by Django 5.1.3 on 2025-01-17 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
