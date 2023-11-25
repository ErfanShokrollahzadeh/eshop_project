from django.shortcuts import render


def index_page(request):
    return render(request, 'home_module/index_page.html')

def site_header_component(request):
    context = {
        'link': 'اموزش چنگو'
    }
    return render(request, 'shared/site_header_partial.html',context)

def site_footer_component(request):
    return render(request, 'shared/site_footer_partial.html',{})