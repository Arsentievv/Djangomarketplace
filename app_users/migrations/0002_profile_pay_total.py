# Generated by Django 4.1.5 on 2023-01-27 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pay_total',
            field=models.IntegerField(default=0),
        ),
    ]
