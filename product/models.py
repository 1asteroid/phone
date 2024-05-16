from django.db import models
from .helpes import SaveImages, CategoryChoise, ColorChoise, SizesProduct, PriceType
from django.contrib.auth.models import User


class SubCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=CategoryChoise, default=CategoryChoise.men)
    subcategory = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    slug = models.SlugField(verbose_name="slug", max_length=100, null=False, unique="True")
    image = models.ImageField(upload_to=SaveImages.product_images_path)
    max_count = models.PositiveIntegerField
    color = models.CharField(max_length=20, choices=ColorChoise, default=ColorChoise.white)
    size = models.CharField(max_length=20, choices=SizesProduct)
    price_type = models.CharField(max_length=5, choices=PriceType, default=PriceType.dollar)
    description = models.TextField

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product
