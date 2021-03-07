from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'is_paid', 'created')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass
