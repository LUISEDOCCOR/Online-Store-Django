from django.db import models

# Create your models here.

class Product (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.PositiveBigIntegerField()
    available = models.BooleanField(default=False)
    text = models.TextField()
    img = models.ImageField(default='null', upload_to='products')