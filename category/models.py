from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=50)