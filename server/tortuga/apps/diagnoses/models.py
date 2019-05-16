"""
Diagnosis model
"""
from django.db import models
from tortuga.apps.symptoms.models import Symptom


class Diagnosis(models.Model):
    """
    Diagnosis attributes
    """
    # Id of this diagnosis
    id = models.BigAutoField(primary_key=True, unique=True, null=False)
    # Symptom id
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    # Name of the diagnosis
    name = models.CharField(max_length=255, null=False)
    # Number of times this diagnosis has been selected
    frequency = models.BigIntegerField(default=0)

    def __str__(self):
        return "SID {}: {}. {} - {}".format(self.symptom.id, self.id, self.name, self.frequency)
