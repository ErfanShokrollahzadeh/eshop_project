from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.CharField(max_length=20, verbose_name='تصویر اواتار', blank=True, null=True)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعال سازی ایمیل', default= True, null=False)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()



# class UserProfile(models.Model):
#     user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
#     phone = models.CharField(max_length=20, blank=True, null=True)
#     address = models.CharField(max_length=100, blank=True, null=True)
#     city = models.CharField(max_length=30, blank=True, null=True)
#     country = models.CharField(max_length=30, blank=True, null=True)
#     zip_code = models.CharField(max_length=10, blank=True, null=True)
#     image = models.ImageField(upload_to='profile_image', blank=True, null=True)
#
#     def __str__(self):
#         return self.user.username
#
#     class Meta:
#         verbose_name_plural = 'User Profile'
