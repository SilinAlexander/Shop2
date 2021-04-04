from rest_framework import serializers
from .models import User, UserCart, Product, Cart


class CartSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = self.context['request'].user
        print(dir(user))
        validated_data['user_cart'] = user.usercart
        return super().create(validated_data=validated_data)

    class Meta:
        model = Cart
        fields = ('product', 'quantity', 'added', 'updated')
        depth = 1


class UserCartSerializer(serializers.ModelSerializer):

    cart_set = CartSerializer(read_only=True, many=True)

    class Meta:
        model = UserCart
        fields = ('owner', 'cart_set')
