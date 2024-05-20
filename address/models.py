from django.db import models
from customer.models import Order


class Country(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class DeliveryAddress(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
