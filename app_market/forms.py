from django import forms

class BalanceUpdate(forms.Form):
    summ_for_update = forms.IntegerField(help_text='Введите сумму для пополнения:')

class BasketForm(forms.Form):
    quantity = forms.IntegerField(help_text='Amount')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class TestForm(forms.Form):
    test = forms.IntegerField(widget=forms.HiddenInput())


