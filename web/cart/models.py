from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from product.models import Product

User = get_user_model()


class UserCart(models.Model):

    owner = models.OneToOneField(User, null=True, verbose_name='Владелец', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)


class Cart(models.Model):

    user_cart = models.ForeignKey(UserCart, verbose_name='Корзина', on_delete=models.CASCADE, related_name='cart_set', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_set', null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    # final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')
    added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.product.name)

