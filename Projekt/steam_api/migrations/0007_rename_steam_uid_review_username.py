# Generated by Django 4.1.2 on 2023-01-11 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('steam_api', '0006_remove_gamer_steam_uid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='steam_uid',
            new_name='username',
        ),
    ]
