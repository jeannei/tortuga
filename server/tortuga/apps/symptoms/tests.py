"""
Tests for Symptom api
"""
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from tortuga.apps.symptoms.models import Symptom
from tortuga.apps.symptoms.serializer import SymptomSerializer


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
            Symptom.objects.create(name=name, frequency=frequency)
        else:
            Symptom.objects.create(name=name)

    def setUp(self):
        """
        Setup symptoms
        """
        self.create_symptom("sore throat")
        self.create_symptom("itchy rash", 5)
        self.create_symptom("runny nose", 300)


class GetAllSymptomsTest(BaseViewTest):
    """
    Test for getting all symptoms
    """
    def test_get_all_symptoms(self):
        """
        This test ensures that all symptoms added in the setUp method
        exist when we make a GET request to the symptoms/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("symptoms-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Symptom.objects.all()
        serialized = SymptomSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
