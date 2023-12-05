from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
# from django.http import HttpResponseRedirect
from .forms import ContactUsForm, ContactUsModelFrom
from django.views.generic import TemplateView


# from .models import ContactUs


class ContactUsView(View):
    def get(self, request):
        contact_form = ContactUsModelFrom()
        return render(request, 'contact_module/contact_us_page.html', {'contact_form': contact_form})

    def post(self, request):
        contact_form = ContactUsModelFrom(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect(reverse('home_page'))
        else:
            return render(request, 'contact_module/contact_us_page.html', {'contact_form': contact_form})



# def contact_us_page(request):
#     if request.method == 'POST':
#         # contact_form = ContactUsForm(request.POST)
#         contact_form = ContactUsModelFrom(request.POST)
#         if contact_form.is_valid():
#             contact_form.save()
#             return redirect(reverse('home_page'))
#     else:
#         # contact_form = ContactUsForm()
#         contact_form = ContactUsModelFrom()
#     return render(request, 'contact_module/contact_us_page.html', {'contact_form': contact_form})
