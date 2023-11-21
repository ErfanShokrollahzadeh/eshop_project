from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='Category Title')
    url_title =  models.CharField(max_length=300, verbose_name='Category URL Title')

    def __str__(self):
        return f'({self.title} - {self.url_title})'

    class Meta:  # change name of table in admin panel from 'product categories' to 'categories
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'

class ProductInformation(models.Model):
    color = models.CharField(max_length=300, verbose_name='Color')
    size = models.CharField(max_length=300, verbose_name='Size')

    def __str__(self):
        return f'({self.color} - {self.size})'


class Product(models.Model):
    title = models.CharField(max_length=300)
    product_information = models.OneToOneField(ProductInformation, on_delete=models.CASCADE, related_name='product_information', verbose_name='complite information', null=True, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products', null=True, verbose_name='product') # connect two table
    price = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=0)
    short_description = models.CharField(max_length=360, null=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True) # samsung galaxy s20 => samsung-galaxy-s20

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"
