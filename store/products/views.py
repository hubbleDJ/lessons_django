from django.shortcuts import render, HttpResponseRedirect
from products.models import Product, ProductCategory, Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.

# Функции = контроллеры = вьюхи = обработчики запросов

def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)

def products(request, category_id=None, page_num: int = 1):

    per_page = 3

    context = {
        'title': 'Store - Каталог',
        'products': Paginator(
            Product.objects.filter(category__id=category_id) if category_id else Product.objects.all(),
            per_page
        ).page(page_num),
        'categorys': ProductCategory.objects.all(),
        'category_id': category_id,
        'page_num': page_num,
    }
    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects. create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
