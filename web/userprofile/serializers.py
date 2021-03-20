from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Address

User = get_user_model()


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ('profile', )


class UserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='profile_set.image')
    phone = serializers.CharField(source='profile_set.phone')
    # address = AddressSerializer(source='profile_set.address_set', many=True)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
            'image',
            'phone',
            # 'address'
        )

        depth = 2
