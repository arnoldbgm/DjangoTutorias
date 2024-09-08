from django.db import models
from cloudinary.models import CloudinaryField

class ProductoModel(models.Model):
   name = models.CharField(max_length=100)
   price = models.DecimalField(max_digits=10, decimal_places=2)
   image = CloudinaryField('image', blank=True, null=True)
