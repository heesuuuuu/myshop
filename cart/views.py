from django.shortcuts import redirect, render, get_object_or_404
from products.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart = request.session.get('cart', {})
    items = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': product.price * quantity
        })
        total_price += product.price * quantity


    return render(request, 'cart/cart_detail.html', {
        'items': items,
        'total_price': total_price
    })

from django.views.decorators.http import require_POST

@require_POST
def update_cart(request, product_id):
    quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[str(product_id)] = quantity
    else:
        cart.pop(str(product_id), None)  # 0 이하면 제거

    request.session['cart'] = cart
    return redirect('cart_detail')


@require_POST
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('cart_detail')
