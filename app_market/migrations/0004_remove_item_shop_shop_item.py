# Generated by Django 4.1.5 on 2023-01-24 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_market', '0003_remove_shop_item_item_shop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='shop',
        ),
        migrations.AddField(
            model_name='shop',
            name='item',
            field=models.ManyToManyField(to='app_market.item'),
        ),
    ]
