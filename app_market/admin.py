from django.contrib import admin

from app_market.models import Shop, Item


class ShopAdmin(admin.ModelAdmin):
    list_display = ['title']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'amt']

admin.site.register(Shop, ShopAdmin)
admin.site.register(Item, ItemAdmin)
