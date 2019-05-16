"""
Base test class for diagnosis contains common functions
"""

from rest_framework.test import APITestCase, APIClient
from tortuga.apps.diagnoses.models import Diagnosis
from tortuga.apps.symptoms.__tests__.base import BaseViewTest as SymptomViewTest

API_VERSION_V1 = "v1"
VERSION = "version"
SID = "sid"


class BaseViewTest(APITestCase):
    """
    Scaffold diagnosis
    """
    client = APIClient()

    @staticmethod
    def create_diagnosis(symptom, name="", frequency=0):
        """
        Create diagnosis
        """
        if name != "" and frequency > 0:
            return Diagnosis.objects.create(name=name, frequency=frequency, symptom=symptom)
        else:
            return Diagnosis.objects.create(name=name, symptom=symptom)

    def setUp(self):
        """
        Setup diagnosis
        """
        symptom = self.create_symptom("sore throat")
        self.create_diagnosis(symptom, "common cold")
        self.create_diagnosis(symptom, "viral throat infection", 5)
        self.create_diagnosis(symptom, "middle ear infection", 300)
        self.valid_symptom_id = 1
        self.invalid_symptom_id = 200
        self.valid_diagnosis_id = 1
        self.valid_diagnosis_id_alt = 3
        self.invalid_diagnosis_id = 100

    @staticmethod
    def create_symptom(name):
        return SymptomViewTest.create_symptom(name=name)
