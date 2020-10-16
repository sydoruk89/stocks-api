from django.urls import path
from .views import StockList, StockDetail

urlpatterns = [
    path('', StockList.as_view(), name='stock_list'),
    path('<int:pk>', StockDetail.as_view(), name='stock_detail')
]