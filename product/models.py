from django.db import models
from django.db.models import Avg
from django.utils.text import slugify
from rest_framework.reverse import reverse

from .helpes import SaveImages, CategoryChoise, ColorChoise, SizesProduct, PriceType, SaveImagesCategory
from django.contrib.auth.models import User
import uuid


class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=SaveImagesCategory.product_images_path, default="category")

    def __str__(self):
        return self.name

    def product_count(self, p):
        count = p.filter(subcategory=self).count()
        return count

    class Meta:
        ordering = ["id"]
        indexes = [
            models.Index(fields=['id'])
        ]


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(verbose_name="slug", max_length=100, blank=False, unique=True)
    category = models.CharField(max_length=10, choices=CategoryChoise, default=CategoryChoise.men)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    price_type = models.CharField(max_length=5, choices=PriceType, default=PriceType.dollar)
    image = models.ImageField(upload_to=SaveImages.product_images_path)
    max_count = models.PositiveIntegerField()
    color = models.CharField(max_length=20, choices=ColorChoise, default=ColorChoise.white)
    size = models.CharField(max_length=20, choices=SizesProduct)
    description = models.TextField()
    is_discount = models.BooleanField(default=False)
    discount_price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    view_count = models.PositiveBigIntegerField(default=0, blank=False)
    data_added = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["id"]
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("index", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.name}{uuid.uuid4()}")

        return super().save(*args, **kwargs)

    def delete_product(self):
        if self.max_count == 0:
            self.delete()

    def avg_rating(self):

        avg = Review.objects.filter(product=self).aggregate(Avg('rating'))['rating__avg']
        return avg


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    def get_user_name(self):
        user = User.objects.get(id=self.user)
        return f"{user.first_name} {user.last_name}"

    class Meta:
        ordering = ["id"]
        indexes = [
            models.Index(fields=['id'])
        ]
