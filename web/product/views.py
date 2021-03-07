from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import View

from .models import Product, Category





class ProductDetailView(DetailView):


    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CategoryDetailView(DetailView):

    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['category_products'] = Product.objects.filter(category=self.get_object())
        category = self.get_object()
        context['category_products'] = category.product_set.all()
        return context



