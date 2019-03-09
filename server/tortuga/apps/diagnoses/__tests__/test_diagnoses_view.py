"""
Tests for Diagnosis View
"""
from django.urls import reverse
from rest_framework import status
from tortuga.apps.diagnoses.models import Diagnosis
from tortuga.apps.diagnoses.serializer import DiagnosisSerializer
from tortuga.apps.diagnoses.__tests__.base import BaseViewTest, API_VERSION_V1, VERSION


ENDPOINT = "diagnoses-all"


class DiagnosesViewTest(BaseViewTest):
    """
    Tests for getting all diagnoses
    """
    def test_get_all_diagnoses(self):
        """
        This test ensures that all diagnoses added in the setUp method
        exist when we make a GET request to the diagnoses/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(reverse(ENDPOINT, kwargs={VERSION: API_VERSION_V1}))
        # fetch the data from db
        expected = Diagnosis.objects.all()
        serialized = DiagnosisSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
