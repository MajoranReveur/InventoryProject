from django.db import models

# Create your models here.

class Food(models.Model):
    gtin = models.IntegerField()
    peremption = models.DateField()
