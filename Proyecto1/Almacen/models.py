from django.db import models

# Create your models here.
class ModelProducts(models.Model):
     nombreProduct=models.CharField(max_length=254, null=False);
     fechaProduct = models.CharField(max_length=254, null=False);
     fechaCaducidad= models.CharField(max_length=254, null=False);
     cantidad = models.IntegerField(null=False);
     venta= models.CharField(max_length=254, null=False);
     

