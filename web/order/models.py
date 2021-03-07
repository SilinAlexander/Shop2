from django.contrib.auth import get_user_model
from django.db import models
from userprofile.models import Address
from product.models import Product

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_set', blank=True, null=True)
    # session
    created = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING, related_name='order_set')
    objects = models.Manager()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item_set')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='order_item_set', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1)
    objects = models.Manager()

    class Meta:
        unique_together = ('product', 'order')
