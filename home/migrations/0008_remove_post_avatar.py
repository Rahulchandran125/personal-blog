# Generated by Django 5.1.3 on 2025-01-17 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_post_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='avatar',
        ),
    ]
