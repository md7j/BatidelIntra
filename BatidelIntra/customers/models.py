from django.db import models

class Customer(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    phone = models.CharField(max_length=33)
    port = models.CharField(max_length=33)
