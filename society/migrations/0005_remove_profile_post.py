# Generated by Django 3.1.2 on 2020-12-22 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('society', '0004_profile_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='post',
        ),
    ]
