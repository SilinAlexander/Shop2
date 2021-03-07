from django.contrib import admin
from .models import Cart, UserCart

# Register your models here.
admin.site.register(UserCart)
admin.site.register(Cart)
