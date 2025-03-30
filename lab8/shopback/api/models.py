from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField
    count = models.IntegerField()
    is_active = models.BooleanField
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name