from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=1023)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Offer(models.Model):
    code = models.CharField(max_length=40)
    description = models.CharField(max_length=255)
    discount = models.FloatField()


