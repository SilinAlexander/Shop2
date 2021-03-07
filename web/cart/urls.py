from django.urls import path

from . import views


urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart'),
    path('add-to-cart/<str:slug>/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('delete-from-cart/<slug>/', views.DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:slug>/', views.ChangeQTYView.as_view(), name='change_qty'),

]
