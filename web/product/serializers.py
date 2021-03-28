from rest_framework import serializers
from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True, min_value=1)
    url = serializers.CharField(source='get_absolute_url')

    class Meta:
        model = Product
        fields = ('title', 'url', 'description', 'category', 'price', 'category_id', 'id')


class BaseCategorySerializer(serializers.ModelSerializer):

    url = serializers.CharField(source='get_absolute_url')

    class Meta:
        model = Category
        fields = ('id', 'name', 'url', )


class CategorySerializer(BaseCategorySerializer):

    products = ProductSerializer(source='product_set', many=True)

    class Meta(BaseCategorySerializer.Meta):
        fields = BaseCategorySerializer.Meta.fields + ('products', )

        depth = 1






