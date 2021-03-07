from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from product.models import Product

User = get_user_model()


class UserCart(models.Model):

    owner = models.OneToOneField(User, null=True, verbose_name='Владелец', on_delete=models.CASCADE)
    # products = models.ManyToManyField('CartProduct', blank=True, related_name='related_cart')
    # total_products = models.PositiveIntegerField(default=0)
    # final_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Общая цена')
    # in_order = models.BooleanField(default=False)
    # for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        # cart_data = self.products.aggregate(models.Sum('final_price'), models.Count('id'))
        # if cart_data.get('final_price__sum'):
        #     self.final_price = cart_data['final_price__sum']
        # else:
        #     self.final_price = 0
        # self.total_products = cart_data['id__count']
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

