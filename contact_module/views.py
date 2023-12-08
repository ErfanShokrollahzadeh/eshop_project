from django.shortcuts import render, redirect
# from django.urls import reverse
from django.views import View
from django.views.generic import ListView

# from django.http import HttpResponseRedirect
# from django.views.generic import TemplateView
from .forms import ContactUsModelFrom
from django.views.generic.edit import FormView, CreateView
from .models import ContactUs, UserProfile


class ContactUsView(CreateView):
    form_class = ContactUsModelFrom
    template_name = 'contact_module/contact_us_page.html'
    success_url = '/contact_us/'


def store_file(file):
    with open('temp/image.jpg', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)



class CreateProfileView(CreateView):
    template_name = 'contact_module/create-profile-page.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact-us/create-profile'


class ProfileView(ListView):
    template_name = 'contact_module/profiles_list_page.html'
    model = UserProfile
    context_object_name = 'profiles'