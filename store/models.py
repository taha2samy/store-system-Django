from django.db import models
from django.db.models.signals import *
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Store(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    def __str__(self) -> str:
        return str(f'{self.category} ')
