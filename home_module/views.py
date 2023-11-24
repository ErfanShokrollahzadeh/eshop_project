from django.shortcuts import render


def index_page(request):
    return render(request, 'home_module/index_page.html')