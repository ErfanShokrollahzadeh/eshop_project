from django import forms
from django.core import validators


class RegisterForm(forms.Form):
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput,
                             validators=[validators.MaxLengthValidator(100), validators.EmailValidator])
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)
    confrim_password = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput)

    def clean_confrim_password(self):
        password = self.cleaned_data.get('password')
        confrim_password = self.cleaned_data.get('confrim_password')
        if password != confrim_password:
            raise forms.ValidationError('رمز عبور و تکرار آن یکسان نیستند')
        return confrim_password