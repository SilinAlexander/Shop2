from django.shortcuts import render
from django.views import View
from .services import OrderService


class CreateOrderView(View):

    def get(self, request):
        service = OrderService(request)
        #order =
        #session cart,
        #create Order
        #save in OrderItem
        #
        return render(request, 'order/order.html', { })

