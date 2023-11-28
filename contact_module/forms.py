from django import forms
from .models import ContactUs


class ContactUsForm(forms.Form):
    full_name = forms.CharField(max_length=50, label='نام و نام خانوادگی',
        error_messages={'max_length': 'لطفا نام و نام خانوادگی نمی تواند بیشتر از ۵۰ کاراکتر باشد'},
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام نام خانوادگی'}))

    email = forms.EmailField(max_length=300, label='ایمیل',
            widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'ایمیل'}))

    title = forms.CharField(max_length=300, label='عنوان',
            widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'عنوان'}))

    message = forms.CharField(label='متن پیام',
            widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'متن پیام', 'id':'message', 'rows':'5'}))



# the bottom class for conetc to contact us model in models.py
class ContactUsModelFrom(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['title', 'full_name', 'email', 'message'] # or for all we can use fields: '__all__'
        # exclude=['response'] # it's mean I just don't want to show this field in form