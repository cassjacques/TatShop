# Generated by Django 3.1.6 on 2021-02-08 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210208_0003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='flash',
            new_name='flashs',
        ),
    ]
