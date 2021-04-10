from django_filters import rest_framework as filters
from .models import UserCart


class CartFilter(filters.FilterSet):
    product = filters.CharFilter(field_name='cart_set__product__title', lookup_expr='icontains')
    min_price = filters.NumberFilter(field_name='cart_set__price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='cart_set__price', lookup_expr='lte')

    class Meta:
        model = UserCart
        fields = ('product', 'min_price', 'max_price')