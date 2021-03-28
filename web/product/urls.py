from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('categories', views.CategoryViewSet, basename='categories')

urlpatterns = [
    # path('products/<str:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    # path('categories/', views.CategoryView.as_view()),
    path('categories/list/', views.CategoryViewSet.as_view({'get': 'category_list'}))


]
urlpatterns += router.urls