from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View

from app_market.cart import Cart
from app_market.forms import BalanceUpdate, BasketForm, TestForm
from app_market.models import Item, Shop, History
from django.db.models import Count, Max


class MainPaigeView(generic.TemplateView):
    """Представление - главная страница маркетплейса"""
    template_name = 'app_market/main_paige.html'


class AccountDetail(generic.DetailView):
    """Представление с информацией об аккаунте пользователя"""
    model = User
    template_name = 'app_market/account_detail.html'
    context_object_name = 'user_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['history'] = History.objects.filter(user=self.request.user)
        return context

    def get_object(self, queryset=None):
        return self.request.user


class ReplenishBalanceView(View):
    """Представление ждя пополнения балаонса пользователя"""
    def get(self, request):
        form = BalanceUpdate
        balance = request.user.profile.balance
        return render(request, 'app_market/balance_replenish.html',
                      context={'form': form, 'balance': balance})

    def post(self, request):
        form = BalanceUpdate(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                amt = form.cleaned_data.get('summ_for_update')
                update = request.user.profile.UpadateBalance(amt)
                request.user.profile.save()
                return HttpResponseRedirect('/market/account_detail/')
        return render(request, 'app_market/balance_replenish.html',
                      context={'form': form})

class ItemListView(generic.ListView):
    """Представление для отображения списка магазинов и товаров в них"""
    model = Item
    template_name = 'app_market/item_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shop = Shop.objects.prefetch_related('item').all()
        context['shop_list'] = shop
        return context

class ItemDetail(generic.DetailView):
    """Представление для детализации информации о товаре"""
    model = Item
    template_name = 'app_market/item_detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BasketForm
        return context

    def post(self, request, **kwargs):
        cart = Cart(request)
        item = get_object_or_404(Item, id=kwargs.get('pk'))
        form = BasketForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(item=item,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
        return redirect('/market/account_detail/cart/')

class CartDetail(View):
    """Представление с детальной информацией о корзине пользователя"""

    def get(self, request):
        cart = Cart(request)
        form = TestForm()
        return render(request, 'app_market/cart_detail.html', {'cart': cart, 'form': form})

    @transaction.atomic
    def post(self, request):
        form = TestForm(request.POST)
        cart = Cart(request)
        if request.user.profile.balance >= cart.get_total_price():
            new_balance = request.user.profile.UpadateBalance(-cart.get_total_price())
            request.user.profile.UpdatePayTotal(cart.get_total_price())
            request.user.profile.save()
            for item in cart.__iter__():
                instance = Item.objects.get(id=int(list(item.values())[2].id))
                if instance.amt > 0:
                    quantity = item['quantity']
                    instance.amt -= item['quantity']
                    instance.sell_amt += item['quantity']
                    History.objects.create(user=request.user, item=instance, quantity=quantity)
                    instance.save()
                else:
                    return HttpResponse('Out of stock')
            cart.clear()
            return redirect('/market/main/')
        else:
            return render(request, 'app_market/cart_detail.html', {'cart': cart, 'form': form})


class ReportView(View):
    """Представление с отчетом наиболее продаваемых товаров"""
    def get(self, request):
        best_sellers = History.objects.annotate(count=Count('quantity')).order_by('-quantity')[0:5]
        return render(request, 'app_market/report.html', context={'best_sellers': best_sellers})












