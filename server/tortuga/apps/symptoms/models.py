"""
Symptom model
"""
from django.db import models


class Symptom(models.Model):
    """
    Symptom attributes
    """
    # Id of this symptom
    id = models.BigAutoField(primary_key=True, unique=True, null=False)
    # Name of the symptom
    name = models.CharField(max_length=255, null=False)
    # Number of times this symptom has been selected
    frequency = models.BigIntegerField(default=0)

    def __str__(self):
        return "{}. {} - {}".format(self.id, self.name, self.frequency)
