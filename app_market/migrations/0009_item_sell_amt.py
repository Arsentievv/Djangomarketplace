# Generated by Django 4.1.5 on 2023-01-28 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_market', '0008_cart_delete_basket'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sell_amt',
            field=models.IntegerField(default=0, verbose_name='Sell times'),
        ),
    ]
