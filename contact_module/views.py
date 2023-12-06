from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
# from django.http import HttpResponseRedirect
from .forms import ContactUsForm, ContactUsModelFrom
from django.views.generic import TemplateView
from django.views.generic.edit import FormView


# from .models import ContactUs


class ContactUsView(FormView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelFrom
    success_url = '/contact_us/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)