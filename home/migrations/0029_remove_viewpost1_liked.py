# Generated by Django 5.1.3 on 2025-01-26 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_viewpost1_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viewpost1',
            name='liked',
        ),
    ]
