# Generated by Django 2.2.28 on 2024-02-04 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_page_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='page',
            name='views',
        ),
    ]
