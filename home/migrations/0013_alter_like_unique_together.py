# Generated by Django 5.1.3 on 2025-01-22 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_like_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set(),
        ),
    ]
