from django.shortcuts import render, redirect
from django.urls import reverse
# from django.http import HttpResponseRedirect
from .forms import ContactUsForm, ContactUsModelFrom
from .models import ContactUs


def contact_us_page(request):
    # if request.method == 'POST':
    #     entered_email = request.POST['email']
    #     if entered_email == '':
    #         return render(request, 'contact_module/contact_us_page.html', {'has_error': True})
    #     print(request.POST['email'])
    #     print(request.POST['fullname'])
    #     print(request.POST['subject'])
    #     print(request.POST['message'])
    #     return redirect(reverse('home_page'))

    if request.method == 'POST':
        # contact_form = ContactUsForm(request.POST)
        contact_form = ContactUsModelFrom(request.POST)
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
            contact = ContactUs(
                title = contact_form.cleaned_data.get('title'),
                full_name=contact_form.cleaned_data.get('full_name'),
                email=contact_form.cleaned_data.get('email'),
                message=contact_form.cleaned_data.get('message'),
            )
            contact.save()
            return redirect(reverse('home_page'))
    else:
        # contact_form = ContactUsForm()
        contact_form = ContactUsModelFrom()
    return render(request, 'contact_module/contact_us_page.html', {'contact_form': contact_form})
