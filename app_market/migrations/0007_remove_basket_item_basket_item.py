# Generated by Django 4.1.5 on 2023-01-26 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_market', '0006_item_amt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='item',
        ),
        migrations.AddField(
            model_name='basket',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_market.item'),
            preserve_default=False,
        ),
    ]
