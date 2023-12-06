from django.shortcuts import render, redirect
# from django.urls import reverse
from django.views import View
# from django.http import HttpResponseRedirect
# from django.views.generic import TemplateView
from .forms import ContactUsModelFrom, ProfileForm
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



class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, 'contact_module/create-profile-page.html', {'form': form})

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            # store_file(request.FILES['profile'])
            profile = UserProfile(image=request.FILES['user_image'])
            profile.save()
            return redirect('/contact_us/create-profile/')
        return render(request, 'contact_module/create-profile-page.html', {'form': submitted_form})




