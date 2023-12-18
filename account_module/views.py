from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest
# from django.contrib.auth import get_user_model
from django.views import View
from account_module.forms import RegisterForm
from .models import User
from django.utils.crypto import get_random_string
from django.http import Http404
from .forms import LoginForm
from django.contrib.auth import login, logout


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
                register_form.add_error('email', 'ایمیل واد شده تکراری می باشد')
            else:
                new_user = User(email=user_email, email_active_code=get_random_string(length=72), is_active=False,
                                username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                # todo : send email active code
                return redirect(reverse('login_page'))

        context = {'register_form': register_form}
        return render(request, 'account_module/register.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm
        context = {'login_form': login_form}
        return render(request, 'account_module/login.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            if not User.objects.filter(email__iexact=user_email).exists():
                login_form.add_error('email', 'کاربری با این مشخصات یافت نشد')
            user_password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=login_form.cleaned_data.get('email')).first()
            if user is not None:
                if  not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نیست')
                else:
                    is_password_correct = user.check_password(user_password)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('home_page'))
                    else:
                        login_form.add_error('email', 'کاربری یافت نشد')
            else:
                login_form.add_error('email', 'کاربری با این مشخصات یافت نشد')

        context = {'login_form': login_form}
        return render(request, 'account_module/login.html', context)


class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(length=72)
                user.save()
                # todo show success message
                return redirect(reverse('login_page'))
            else:
                # todo show your account was activated message
                pass

        raise Http404('کاربر یافت نشد')
