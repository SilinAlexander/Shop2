from django.urls import path
from .views import CreateOrderView
app_name = 'order'

urlpatterns = [
    path('order/create/', CreateOrderView.as_view(), name='create')

]
