from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    balance = models.IntegerField(default=0, verbose_name='Balance')
    status = models.CharField(default='green', max_length=20, verbose_name='Status')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None)
    pay_total = models.IntegerField(default=0)

    def UpadateBalance(self, amt):
        self.balance += amt

    def UpdatePayTotal(self, amt):
        self.pay_total += amt
        if self.pay_total >= 500:
            self.status = 'bronze'
        elif self.pay_total >= 1000:
            self.status = 'silver'
        elif self.pay_total >= 1500:
            self.status = 'gold'
