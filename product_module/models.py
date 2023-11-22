from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='Category Title')
    url_title =  models.CharField(max_length=300, verbose_name='Category URL Title')
    is_active = models.BooleanField(default=False, verbose_name='Active / UnActive')
    is_delete = models.BooleanField(default=False, verbose_name='Deleted / UnDelete')


    def __str__(self):
        return f'({self.title} - {self.url_title})'

    class Meta:  # change name of table in admin panel from 'product categories' to 'categories
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'

class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='Product Title')
    category = models.ManyToManyField(ProductCategory, related_name='product_categories', verbose_name='categories') # connect two table
    price = models.IntegerField(verbose_name='Price')
    short_description = models.CharField(max_length=360, db_index=True, null=True, verbose_name='Short Description')
    description = models.TextField(verbose_name="Main Description", db_index=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True, verbose_name='Title in url') # samsung galaxy s20 => samsung-galaxy-s20
    is_active = models.BooleanField(default=False, verbose_name='Active / UnActive')
    is_delete = models.BooleanField(default=False, verbose_name='Deleted / UnDelete')

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"


class ProductTag(models.Model):
    caption= models.CharField(max_length=300, db_index=True, verbose_name='Tag Title')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags', verbose_name='products')

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return f'{self.caption}'