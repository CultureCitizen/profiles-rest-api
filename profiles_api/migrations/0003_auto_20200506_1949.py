# Generated by Django 2.2 on 2020-05-06 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_auto_20200505_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='birth_year',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
    ]
