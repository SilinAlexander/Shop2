from django.contrib import admin
from .models import Profile, Address


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass