# Generated by Django 4.2.7 on 2023-12-26 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_delete_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(default='null', upload_to='products'),
        ),
    ]
