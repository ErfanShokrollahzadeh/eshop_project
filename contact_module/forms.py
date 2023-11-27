from django import forms

class ContactUsForm(forms.Form):
    fullname = forms.CharField(max_length=300, label='نام و نام خانوادگی')
    email = forms.EmailField(max_length=300, label='ایمیل', widget=forms.EmailInput)
    subject = forms.CharField(max_length=300, label='عنوان')
    text = forms.CharField(widget=forms.Textarea, label='متن پیام')
