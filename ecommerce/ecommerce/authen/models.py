from django.db import models


class Register(models.Model):
    first_name = models.CharField(max_length=60, unique=True)
    last_name = models.CharField(max_length=60, unique=True)
    phone_no = models.CharField(max_length=60, unique=True)
    email = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=60, unique=True)

# Create your models here.
