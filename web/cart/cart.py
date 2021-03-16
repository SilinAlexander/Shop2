from decimal import Decimal

from django.conf import settings

from product.models import Product


class SessionCart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product_id, qty=1):
        product_price = Product.objects.get(id=product_id).price
        product_id = str(product_id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': qty, 'price': str(product_price)}
        else:
            qty = int(self.cart[product_id]['quantity']) + int(qty)
            self.cart[product_id]['quantity'] = qty

        self.save()

    def save(self):
        self.session.modified = True

    def delete(self, product_id, qty=1):
        product_price = Product.objects.get(id=product_id).price
        product_id = str(product_id)
        if product_id in self.cart:
            self.cart[product_id] = {'quantity': qty, 'price': str(product_price)}
            del self.cart[product_id]
            self.save()

    def update(self, product_id, qty=1):
        product_id = str(product_id)
        self.cart[product_id]['quantity'] = qty

        self.save()

    def __iter__(self):
        cart = self.cart.copy()
        products_id = cart.keys()
        products = Product.objects.filter(id__in=products_id)
        print(products)
        total: dict = {
            'final_price': 0,
            'count': 0
        }
        for product in products:
            product_id = str(product.id)
            cart[product_id]['product'] = product
            total_price = int(product.price) * int(cart[product_id]['quantity'])
            cart[product_id]['total_price'] = total_price
            total['final_price'] += total_price
            total['count'] +=1

        for item in cart.values():

            yield item

    def __len__(self):
        count = []
        for item in self.cart.values():
            count.append(int(item['quantity']))
        return sum(count)

    def get_final_price(self):
        return sum(Decimal(item['price'])*int(item['quantity']) for item in self.cart.values())



