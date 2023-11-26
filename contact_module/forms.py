from django import forms

class ContactUsForm(forms.Form):
    fullname = forms.CharField(max_length=300, label='full name')
    email = forms.EmailField(max_length=300, label='email')
    subject = forms.CharField(max_length=300, label='subject')
    text = forms.CharField(widget=forms.Textarea, label='message')