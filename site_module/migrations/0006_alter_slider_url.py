# Generated by Django 5.0 on 2023-12-22 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0005_alter_slider_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='url',
            field=models.CharField(max_length=500, verbose_name='لینک'),
        ),
    ]
