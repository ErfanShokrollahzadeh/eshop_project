# Generated by Django 4.2.7 on 2023-11-22 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='Deleted / UnDelete'),
        ),
    ]
