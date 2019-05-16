"""
Base test class for symptom contains common functions
"""

from rest_framework.test import APITestCase, APIClient
from tortuga.apps.symptoms.models import Symptom

API_VERSION_V1 = "v1"
VERSION = "version"


class BaseViewTest(APITestCase):
    """
    Scaffold symptoms
    """
    client = APIClient()

    @staticmethod
    def create_symptom(name="", frequency=0):
        """
        Create symptom
        """
        if name != "" and frequency > 0:
            return Symptom.objects.create(name=name, frequency=frequency)
        else:
            return Symptom.objects.create(name=name)

    def setUp(self):
        """
        Setup symptoms
        """
        self.create_symptom("sore throat")
        self.create_symptom("itchy rash", 5)
        self.create_symptom("runny nose", 300)
        self.valid_symptom_id = 1
        self.valid_symptom_id_alt = 3
        self.invalid_symptom_id = 100
