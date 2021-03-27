from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'get_absolute_url', 'product_set')

        depth = 1


class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True, min_value=1)

    class Meta:
        model = Product
        fields = ('title', 'get_absolute_url', 'description', 'category', 'price', 'category_id')

        depth = 1



