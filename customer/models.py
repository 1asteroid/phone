from django.db import models
from django.contrib.auth.models import User
from .helpes import SaveImages
from product.models import Product


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(upload_to=SaveImages.customer_images_path, default="customer_image/default_image.jpg")


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)


class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

