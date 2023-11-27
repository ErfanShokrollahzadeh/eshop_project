from django import forms

class ContactUsForm(forms.Form):
    fullname = forms.CharField(max_length=50, label='نام و نام خانوادگی',
        error_messages={'max_length': 'لطفا نام و نام خانوادگی نمی تواند بیشتر از ۵۰ کاراکتر باشد'},
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'نام نام خانوادگی'}))

    email = forms.EmailField(max_length=300, label='ایمیل',
            widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'ایمیل'}))

    subject = forms.CharField(max_length=300, label='عنوان',
            widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'عنوان'}))

    text = forms.CharField(label='متن پیام',
            widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'متن پیام', 'id':'message', 'rows':'5'}))
