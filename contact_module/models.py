from django.db import models

class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='title')
    email = models.EmailField(max_length=300, verbose_name='email')
    full_name = models.CharField(max_length=300, verbose_name='full name')
    message = models.TextField(verbose_name='massage')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='created date') # auto_now_add=True means that this field will be filled automatically with the current date when the object is created
    response = models.TextField(blank=True, null=True, verbose_name='response')
    is_read_by_admin = models.BooleanField(default=False, verbose_name='is read by admin')


    class Meta:  # change name of table in admin panel from 'product brands' to 'brands
        verbose_name = 'contact us'
        verbose_name_plural = 'contact us list'

    def __str__(self):
        return f'{self.title}'


class UserProfile(models.Model):
    image = models.ImageField(upload_to='images', verbose_name='image')