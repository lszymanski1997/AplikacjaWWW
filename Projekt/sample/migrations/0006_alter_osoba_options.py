# Generated by Django 4.1.2 on 2022-10-19 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0005_alter_osoba_miesiac_urodzenia'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'ordering': ['nazwisko'], 'verbose_name_plural': 'Osoby'},
        ),
    ]