from django.contrib.auth.models import AnonymousUser

from .models import OrderItem, Order
from cart.cart import SessionCart
from .models import User
from product.models import Product


class OrderService:

    def __init__(self, request):
        self.cart = SessionCart(request)
        print(self.cart)
        print(self.cart.cart)
        self.request = request
        self.user = self.get_user()
        self.address = self.check_delivery_address()
        self.order = self.create_order()
        self.order_item = self.add_items_to_order()

    def get_user(self):
        if isinstance(self.request.user, User):
            return self.request.user
        # if isinstance(self.request.user, AnonymousUser):
        #     print('AnonUser')

    def create_order(self):
        return Order.objects.create(user=self.user, address=self.address, is_paid=False)

    def check_delivery_address(self):
        if self.user.profile_set.address_set.exists():
            print('address exists')
            return self.user.profile_set.address_set.first()

    def add_items_to_order(self):
        order_obj =[]
        for product_id, data in self.cart.cart.items():
            print(product_id, data)
            product = Product.objects.get(id=product_id)
            order_item = OrderItem(order=self.order, product=product, price=product.price, quantity=data['quantity'])
            order_obj.append(order_item)
        return OrderItem.objects.bulk_create(order_obj)