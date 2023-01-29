from django.urls import path

from app_market.views import (MainPaigeView,
                              AccountDetail,
                              ReplenishBalanceView,
                              ItemListView,
                              CartDetail,
                              ItemDetail,
                              ReportView
                              )

urlpatterns = [
    path('main/', MainPaigeView.as_view(), name='main'),
    path('account_detail/', AccountDetail.as_view(), name='account_detail'),
    path('account_detail/balance/', ReplenishBalanceView.as_view(), name='balance'),
    path('account_detail/cart/', CartDetail.as_view(), name='cart'),
    path('item_list/', ItemListView.as_view(), name='item_list'),
    path('item_list/<int:pk>/', ItemDetail.as_view(), name='item_detail'),
    path('report/', ReportView.as_view(), name='report')

]