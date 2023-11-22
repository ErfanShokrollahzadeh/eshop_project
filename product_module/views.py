from django.shortcuts import render
from .models import Product, ProductCategory
from django.http import Http404
from django.db.models import Avg, Max, Min

def product_list(request):
    products = Product.objects.all()
    number_of_products = products.count()
    return render(request, 'product_module/product_list.html',
                  {'products': products,
                   'total_number_of_products': number_of_products,
    })

def product_detail(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except:
        raise Http404()
    # product = get_object_or_404(Product, pk=product_id)==> this code working instent of try and except
    return render(request, 'product_module/product_detail.html', {'product': product})