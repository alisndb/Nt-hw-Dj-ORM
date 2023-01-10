from django.db import models


class Phone(models.Model):
    id = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    image = models.CharField(max_length=128)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=64, unique=True)
