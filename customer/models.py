from django.db import models
from django.contrib.auth.models import User
from .helpes import SaveImages
from product.models import Product


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to=SaveImages.customer_images_path, default="customer_image/default_image.jpg")


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name="slug", max_length=100, null=True, blank=False, unique=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        indexes = [
            models.Index(fields=['id'])
        ]

    def __str__(self):
        name = User.objects.get(username=self.user).first_name
        return f"order of {name}"


class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    complete = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        indexes = [
            models.Index(fields=['id'])
        ]

    def total_item(self):
        return self.product.price * self.quantity

    def check_count(self):
        if self.complete and self.product.max_count < self.quantity:
            self.quantity = self.product.max_count


class Appeal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    answered = models.BooleanField(default=False)
