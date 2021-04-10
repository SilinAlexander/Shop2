from rest_framework import serializers
from .models import User, UserCart, Product, Cart


class CartSerializer(serializers.ModelSerializer):

    product_id = serializers.IntegerField(min_value=1, write_only=True)

    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     print(dir(user))
    #     validated_data['user_cart'] = user.usercart
    #     return super().create(validated_data=validated_data)

    def save(self, **kwargs):
        user = self.context['request'].user
        user_cart = user.usercart_set
        obj, created = Cart.objects.update_or_create(#created: True - объект добавлен, False -объект обновлен
            product_id=self.validated_data.get('product_id'),
            user_cart=user_cart,
            defaults={'quantity': self.validated_data.get('quantity')})
        data = self.validated_data
        print(obj, created)

    class Meta:
        model = Cart
        fields = ('product', 'quantity', 'product_id', 'added', 'updated')
        depth = 1


class UserCartSerializer(serializers.ModelSerializer):

    cart_set = CartSerializer(read_only=True, many=True)

    class Meta:
        model = UserCart
        fields = ('owner', 'cart_set')
