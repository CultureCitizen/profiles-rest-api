# Generated by Django 2.2 on 2020-05-05 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='birth_year',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='sex',
        ),
    ]
