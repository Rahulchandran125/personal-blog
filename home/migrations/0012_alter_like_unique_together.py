# Generated by Django 5.1.3 on 2025-01-22 07:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_viewpost1_like_like'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('post', 'user')},
        ),
    ]
