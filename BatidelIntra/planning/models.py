from django.db import models

class SAV(models.Model):
    STATES = (
        ('GOK', 'SOUS_GARANTIE'),
        ('GKO', 'HORS_GARANTIE'),
        ('EOP', 'FIN_DE_CHANTIER'),
        ('EXT', 'SAV_EXTERIEUR'),
    )
    creationDate = models.DateField()
    customer = models.ForeignKey('customers.Customer', on_delete=models.CASCADE)
    state = models.CharField(max_length=3, choices=STATES)
    nature = models.TextField()
    furnitureReception = models.DateField()
    programmation = models.DateField()
    conclusion = models.TextField()