"""
Scaffold sql lite data
"""
from django.core.management.base import BaseCommand
from tortuga.utils.parser import parse_symptoms_csv
from tortuga.apps.symptoms.models import Symptom
from tortuga.apps.diagnoses.models import Diagnosis


class Command(BaseCommand):
    """
    Custom command for loading data
    """

    def handle(self, *args, **options):
        """
        Load initial symptoms into database
        """
        data = parse_symptoms_csv("tortuga/fixtures/symptoms.csv")

        for symptom, diagnoses in data.items():
            persisted_symptom = self._save_symptom(symptom)
            for diagnosis in diagnoses:
                self._save_diagnosis(persisted_symptom, diagnosis)

    @staticmethod
    def _save_diagnosis(symptom, value):
        """
        Save diagnosis
        """
        diagnosis = Diagnosis(symptom=symptom, name=value)
        diagnosis.save()
        return diagnosis

    @staticmethod
    def _save_symptom(value):
        """
        Save symptom
        """
        symptom = Symptom(name=value)
        symptom.save()
        return symptom
