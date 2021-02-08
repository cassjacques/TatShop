# Generated by Django 3.1.6 on 2021-02-07 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210207_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='deets',
            field=models.ManyToManyField(to='main_app.Deets'),
        ),
    ]