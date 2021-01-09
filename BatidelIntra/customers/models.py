from django.db import models


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    address = models.JSONField()
    phone = models.CharField(max_length=33)
    port = models.CharField(max_length=33)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['lastName']

    def __str__(self):
        return self.firstName + " " + self.lastName
