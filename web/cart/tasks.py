from src.celery import app
from .models import Cart, UserCart, User, Product


@app.task
def add_to_cart(user_id, product_id, quantity):
    print(user_id, product_id, quantity)
    user = User.objects.get(id=user_id)
    product = Product.objects.get(id=product_id)
    user_cart = UserCart.objects.get(owner=user)
    user_cart.cart_set.create(product=product, quantity=quantity)
