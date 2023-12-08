from django import forms
from .models import ContactUs


class ContactUsModelFrom(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['title', 'full_name', 'email', 'message'] # or for all we can use fields: '__all__'
        # exclude=['response'] # it's mean I just don't want to show this field in form
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'عنوان'}),
            'full_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام و نام خانوادگی'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'ایمیل'}),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'متن پیام', 'id':'message', 'rows':'5'}),
        }
        labels = {
            'title': 'عنوان',
            'full_name': 'نام و نام خانوادگی',
            'email': 'ایمیل',
            'message': 'متن پیام',
        }
        error_messages = {
            'full_name': {
                'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
                'max_length': 'لطفا نام و نام خانوادگی نمی تواند بیشتر از ۵۰ کاراکتر باشد',
            },
        }

