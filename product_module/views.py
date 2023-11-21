from django.shortcuts import render
from .models import Product, ProductCategory
from django.http import Http404
from django.db.models import Avg, Max, Min

def product_list(request):
    consol = ProductCategory(title = 'play station', url_title = 'play-station')
    consol.save()

    ps_4 = Product(title = 'play station 4', category = consol, price = 1600000, rating = 4, short_description = 'play station 4', is_active = True)
    ps_4.save()

    products = Product.objects.all()
    number_of_products = products.count()
    avg_rating = products.aggregate(Avg('rating')),
    return render(request, 'product_module/product_list.html',
                  {'products': products,
                   'total_number_of_products': number_of_products,
                   'avarage_rating': avg_rating
    })

def product_detail(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except:
        raise Http404()
    # product = get_object_or_404(Product, pk=product_id)==> this code working instent of try and except
    return render(request, 'product_module/product_detail.html', {'product': product})