from django.db import models

# Create your models here.

class Items(models.Model):
    id = models.AutoField(primary_key=True)
    SKU = models.CharField(max_length = 300)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    tags=models.CharField(max_length=100)
    stock_status = models.BooleanField()
    available_stock = models.IntegerField()