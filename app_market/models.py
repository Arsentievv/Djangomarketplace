from django.contrib.auth.models import User
from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=30, verbose_name='Item title')
    description = models.TextField(max_length=200, verbose_name='Item description')
    price = models.PositiveIntegerField(verbose_name='Item price')
    amt = models.PositiveIntegerField(default=1, verbose_name='Item amount')
    sell_amt = models.IntegerField(default=0, verbose_name='Sell times')


class Shop(models.Model):
    title = models.CharField(max_length=30, verbose_name='Shop title')
    item = models.ManyToManyField('Item')


class Cart(models.Model):
    cart_id = models.CharField(max_length=50)
    item = models.ForeignKey('Item', on_delete=models.CASCADE, unique=False)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=0)






