from django.shortcuts import render
from .models import Product
from django.http import Http404


def product_list(request):
    products = Product.objects.all().order_by('-price')[:5]
    return render(request, 'product_module/product_list.html',{'products': products,})

def product_detail(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except:
        raise Http404()
    # product = get_object_or_404(Product, pk=product_id)==> this code working instent of try and except
    return render(request, 'product_module/product_detail.html', {'product': product})
