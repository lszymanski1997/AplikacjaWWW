# Generated by Django 4.1.2 on 2023-01-05 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('steam_api', '0002_user_steam_uid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['name']},
        ),
    ]
