from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm
from django.db.models import Q

def product_list(request):
    category_id = request.GET.get('category')
    query = request.GET.get('q')

    products = Product.objects.all()

    if category_id:
        products = products.filter(category_id=category_id)
    
    if query:
        products = products.filter(name__icontains=query)

    categories = Category.objects.all()

    return render(request, 'products/product_list.html', {
        'products': products,
        'categories': categories,
        'selected_category': category_id
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all() ## related_name을 사용하여 리뷰 가져오기
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', pk=pk)
    else:
        form = ReviewForm()
    return render(request, 'products/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})