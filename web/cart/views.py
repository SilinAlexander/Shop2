from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from .cart import SessionCart
from product.models import Product
from .tasks import add_to_cart


class ProductInCart(View):

    def get(self, request, *args, **kwargs):
        # # categories = Category.objects.get_categories_for_left_sidebar()
        # products = LatestProducts.objects.get_products_for_main_page(
        #     # 'prod1', 'prod2', with_respect_to='prod1'
        # )
        # context = {
        #     # 'categories': categories,
        #     'products': products,
        #     'cart': self.cart
        # }
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
        # cart = SessionCart(request)
        # cart.add(product_id=product.id, qty=qty)
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
        # ct_model, product_slug = kwargs.get('ct_model'), kwargs.get('slug')
        # content_type = ContentType.objects.get(model=ct_model)
        # product = content_type.model_class().objects.get(slug=product_slug)
        # cart_product = CartProduct.objects.get(
        #     user=self.cart.owner, cart=self.cart, content_type=content_type, object_id=product.id
        # )
        # self.cart.products.remove(cart_product)
        # cart_product.delete()
        # self.cart.save()
        product = self.get_object()
        cart = SessionCart(request)
        cart.delete(product_id=product.id)
        messages.add_message(request, messages.INFO, "Товар успешно удален")
        return HttpResponseRedirect('/cart/')

    def get_object(self):
        return get_object_or_404(Product, slug=self.kwargs.get('slug'))


class ChangeQTYView(View):

    def post(self, request, *args, **kwargs):
        # cart_product = CartProduct.objects.get(
        #     user=self.cart.owner, cart=self.cart, content_type=content_type, object_id=product.id
        # )
        # qty = int(request.POST.get('qty'))
        # cart_product.qty = qty
        # cart_product.save()
        # self.cart.save()
        product = self.get_object()
        cart = SessionCart(request)
        cart.update(product_id=product.id, qty=request.POST.get('qty'))
        messages.add_message(request, messages.INFO, "Кол-во успешно изменено")
        return HttpResponseRedirect('/cart/')

    def get_object(self):
        return get_object_or_404(Product, slug=self.kwargs.get('slug'))