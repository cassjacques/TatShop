# Generated by Django 3.1.6 on 2021-02-08 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20210208_0114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='flashes',
            new_name='flashs',
        ),
    ]
