from django.shortcuts import redirect, render, get_object_or_404
from products.models import Product
from django.contrib.auth.decorators import login_required
from .models import CartItem


@login_required
def cart_add(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')


@login_required
def cart_detail(request):
    items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in items)
    return render(request, 'cart/cart_detail.html', {'items': items, 'total_price': total_price})

from django.views.decorators.http import require_POST

@require_POST
@login_required
def cart_update(request, product_id):
    quantity = int(request.POST.get('quantity', 1))
    cart_item = get_object_or_404(CartItem, user=request.user, product__id=product_id)

    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart_detail')


@require_POST
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('cart_detail')
