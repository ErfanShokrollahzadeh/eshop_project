from django.shortcuts import render, redirect
from django.urls import reverse
# from django.http import HttpResponseRedirect


def contact_us_page(request):
    if request.method == 'POST':
        print(request.POST['email'])
        print(request.POST['fullname'])
        print(request.POST['subject'])
        print(request.POST['message'])
        return redirect(reverse('home_page'))
    return render(request, 'contact_module/contact_us_page.html', {})