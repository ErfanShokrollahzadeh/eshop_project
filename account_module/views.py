from django.shortcuts import render
# from django.contrib.auth import get_user_model
from django.views import View
from account_module.forms import RegisterForm
from .models import User
from django.utils.crypto import get_random_string
from django.core.mail import send_mail


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {'register_form': register_form}
        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email','ایمیل واد شده تکراری می باشد')
            else:
                new_user = User.objects.create_user(email=user_email, password=user_password)
                new_user.save()





        context = {'register_form': register_form}
        return render(request, 'account_module/register.html', context)