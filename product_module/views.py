from django.shortcuts import render
from .models import Product
from django.http import Http404

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_module/product_list.html', {'products': products})

def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except:
        raise Http404()
    # product = get_object_or_404(Product, pk=product_id)==> this code working instent of try and except
    return render(request, 'product_module/product_detail.html', {'product': product})