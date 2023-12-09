# from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
# from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import Product
# from django.http import Http404



class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'

    # def get_queryset(self):
    #     base_query = super(ProductListView, self).get_queryset()
    #     data = base_query.filter(is_active=True)
    #     return data


    # def get_context_data(self, **kwargs):         # this code is working instent of model = Product when we use generic list view
    #     products = Product.objects.all().order_by('-price')[:5]
    #     context = super().get_context_data(**kwargs)
    #     context['products'] = products
    #     return context



# def product_list(request):
#     products = Product.objects.all().order_by('-price')[:5]
#     return render(request, 'product_module/product_list.html',{'products': products,})


# def product_detail(request, slug):
#     try:
#         product = Product.objects.get(slug=slug)
#     except:
#         raise Http404()
#     # product = get_object_or_404(Product, pk=product_id)==> this code working instent of try and except
#     return render(request, 'product_module/product_detail.html', {'product': product})



class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        request = self.request
        favorite_product_id = request.session.get('favorite_product')
        context['is_favorite'] = favorite_product_id == str(loaded_product.id)
        return context


    # def get_context_data(self, **kwargs):
    #     try:
    #         product = Product.objects.get(slug=kwargs['slug'])
    #     except:
    #         raise Http404()
    #     context = super().get_context_data(**kwargs)
    #     context['product'] = product
    #     return context

class AddProductFavorite(View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)
        request.session['favorite_product'] = product_id
        return redirect(product.get_absolute_url())
