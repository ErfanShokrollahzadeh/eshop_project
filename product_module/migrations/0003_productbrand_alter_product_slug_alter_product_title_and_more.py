# Generated by Django 4.2.7 on 2023-11-24 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0002_productcategory_is_delete'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300, verbose_name='Brand name')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active / UnActive')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Deleted / UnDelete')),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=200, unique=True, verbose_name='Title in url'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Product Title'),
        ),
        migrations.AlterField(
            model_name='producttag',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_tags', to='product_module.product', verbose_name='products'),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_module.productbrand', verbose_name='brands'),
        ),
    ]