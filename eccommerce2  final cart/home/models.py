from django.db import models
from django.contrib.auth.models import auth, User
# Create your models here.


class Whishlist (models.Model):
    image = models.ImageField(upload_to="whishlist", blank=True, null=True)
    description = models.CharField(max_length=2000)
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    old_id = models.IntegerField()

