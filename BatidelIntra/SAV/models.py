from django.db import models

class SAV(models.Model):
    class States(models.TextChoices):
        SOUS_GARANTIE = 'GOK'
        HORS_GARANTIE = 'GKO'
        FIN_DE_CHANTIER = 'EOP'
        SAV_EXTERIEUR = 'EXT'

    id = models.AutoField(primary_key=True)
    creationDate = models.DateField()
    customer = models.ForeignKey(
        'customers.Customer',
        models.CASCADE,
        verbose_name='customer',
        related_name='SAV'
    )
    address = models.JSONField()
    state = models.CharField(max_length=3, choices=States.choices)
    nature = models.TextField()
    furnitureReception = models.DateField()
    programmation = models.DateField()
    conclusion = models.TextField()

    class Meta:
        ordering = ['creationDate']

    def __str__(self):
        return self.customer.firstName + " " + self.customer.lastName
