from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from .cart import SessionCart
from product.models import Product
from .models import UserCart
from .tasks import add_to_cart
from rest_framework.generics import GenericAPIView
from .serializers import UserCartSerializer, CartSerializer
from rest_framework.response import Response


class ProductInCart(View):

    def get(self, request, *args, **kwargs):
        request.session['cart'] = 'fsrergrfg'
        request.session['cart1'] = 'fsrergrfg'
        print(request.session.items())
        return render(request, 'base.html', {})


class CartView(View):

    def get(self, request, *args, **kwargs):
        cart = SessionCart(request)
        context = {
            'cart': cart
        }
        return render(request, 'cart.html', context)


class AddToCartView(View):

    def post(self, request, *args, **kwargs):

        qty = request.POST.get('qty')
        product = self.get_object()
        print(qty)
        print(request.session.items())
        messages.add_message(request, messages.INFO, "Товар успешно добавлен")
        user_id = request.user.id
        product_id = product.id
        add_to_cart.delay(user_id, product_id, qty)
        return HttpResponseRedirect('/cart/')

    def get_object(self):
        return get_object_or_404(Product, slug=self.kwargs.get('slug'))


class DeleteFromCartView(View):

    def get(self, request, slug, *args, **kwargs):

        product = self.get_object()
        cart = SessionCart(request)
        cart.delete(product_id=product.id)
        messages.add_message(request, messages.INFO, "Товар успешно удален")
        return HttpResponseRedirect('/cart/')

    def get_object(self):
        return get_object_or_404(Product, slug=self.kwargs.get('slug'))


class ChangeQTYView(View):

    def post(self, request, *args, **kwargs):

        product = self.get_object()
        cart = SessionCart(request)
        cart.update(product_id=product.id, qty=request.POST.get('qty'))
        messages.add_message(request, messages.INFO, "Кол-во успешно изменено")
        return HttpResponseRedirect('/cart/')

    def get_object(self):
        return get_object_or_404(Product, slug=self.kwargs.get('slug'))


class GetProductInCartView(GenericAPIView):

    serializer_class = UserCartSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(), owner=self.request.user)

    def get_queryset(self):
        return UserCart.objects.all().prefetch_related('cart_set')

    def get(self, request):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class AddProductTOCartView(GenericAPIView):
    serializer_class = CartSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


