from django.db import models


class Customer(models.Model):
    #    id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    phone = models.CharField(max_length=33)
    port = models.CharField(max_length=33)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['lastName']

    def __str__(self):
        return self.firstName + " " + self.lastName
