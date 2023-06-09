import pytest
from django.contrib.auth.models import User
from shopping.models import Cart

@pytest.mark.django_db
def test_cart_str_representation():
    user = User.objects.create_user(username='testuser', password='testpass')
    cart = Cart.objects.create(user=user)
    assert str(cart) == f"Cart {cart.pk}"
