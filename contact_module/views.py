from django.shortcuts import render, redirect
# from django.urls import reverse
from django.views import View
# from django.http import HttpResponseRedirect
# from django.views.generic import TemplateView
from .forms import ContactUsForm, ContactUsModelFrom
from django.views.generic.edit import FormView, CreateView
from .models import ContactUs


# from .models import ContactUs


class ContactUsView(CreateView):
    form_class = ContactUsModelFrom
    template_name = 'contact_module/contact_us_page.html'
    success_url = '/contact_us/'



class CreateProfileView(View):
    def get(self, request):
        form = ContactUsForm()
        return render(request, 'contact_module/create-profile-page.html', {'form': form})

    def post(self, request):
        print(request.FILES)
        return redirect('/contact_us/create-profile/')