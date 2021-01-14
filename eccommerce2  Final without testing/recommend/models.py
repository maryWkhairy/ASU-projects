from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL


class save_products(models.Model):
    description = models.CharField(max_length=20)
    price = models.FloatField()
    image = models.ImageField(upload_to='recommend')

