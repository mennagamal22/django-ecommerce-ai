from .models import Cart
from django.contrib.auth.models import User

def cart_count(request):
    user = request.user if request.user.is_authenticated else User.objects.first()
    count = 0
    if user:
        try:
            cart = Cart.objects.get(user=user)
            count = sum(item.quantity for item in cart.items.all())
        except Cart.DoesNotExist:
            count = 0
    return {'cart_count': count}