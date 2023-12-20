from django.db import models


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='نام سایت')
    site_url = models.CharField(max_length=200, verbose_name='دامنه سایت')
    address = models.CharField(max_length=200, verbose_name='آدرس')
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='تلفن')
    fax = models.CharField(max_length=200, null=True, blank=True, verbose_name='فکس')
    email = models.EmailField(max_length=200, null=True, blank=True, verbose_name='ایمیل')
    copy_right = models.TextField(verbose_name='متن کپی رایت')
    about_us_text = models.TextField(verbose_name='درباره ما')
    site_logo = models.ImageField(upload_to='images/site-setting/', verbose_name='لوگو سایت')
    is_main_setting = models.BooleanField(default=True, verbose_name='تنظیمات اصلی')

    class Meta:
        verbose_name = 'Site setting'
        verbose_name_plural = 'Setting '

    def __str__(self):
        return self.site_name


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')

    class Meta:
        verbose_name = 'Category of links footer'
        verbose_name_plural = 'Categories of links footer'

    def __str__(self):
        return self.title

class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url  = models.URLField(max_length=500, verbose_name='لینک')
    footer_link_box = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'link footer'
        verbose_name_plural = 'links footer'

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    url_title = models.CharField(max_length=200, verbose_name='عنوان لینک')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='images/sliders/', verbose_name='تصویر')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'slider'
        verbose_name_plural = 'sliders'

    def __str__(self):
        return self.title