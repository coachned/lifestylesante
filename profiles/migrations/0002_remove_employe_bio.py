# Generated by Django 5.1.4 on 2024-12-11 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employe',
            name='bio',
        ),
    ]
