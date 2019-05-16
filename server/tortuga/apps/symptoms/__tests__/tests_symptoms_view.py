"""
Tests for Symptoms View
"""
from django.urls import reverse
from rest_framework import status
from tortuga.apps.symptoms.models import Symptom
from tortuga.apps.symptoms.serializer import SymptomSerializer
from tortuga.apps.symptoms.__tests__.base import BaseViewTest, API_VERSION_V1, VERSION


ENDPOINT = "symptoms-all"


class SymptomsViewTest(BaseViewTest):
    """
    Tests for getting all symptoms
    """
    def test_get_all_symptoms(self):
        """
        This test ensures that all symptoms added in the setUp method
        exist when we make a GET request to the symptoms/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(reverse(ENDPOINT, kwargs={VERSION: API_VERSION_V1}))
        # fetch the data from db
        expected = Symptom.objects.all()
        serialized = SymptomSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_symptom(self):
        """
        This test ensures users cannot create new symptoms
        """
        # hit the API endpoint
        response = self.client.post(
            reverse(ENDPOINT, kwargs={VERSION: API_VERSION_V1}),
            {"name": "test 4", "frequency": 0}
        )

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_symptom(self):
        """
        This test ensures users cannot delete symptoms
        """
        # hit the API endpoint
        response = self.client.delete(
            reverse(ENDPOINT, kwargs={VERSION: API_VERSION_V1}),
            {"name": "test 4", "frequency": 0}
        )

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_symptom(self):
        """
        This test ensures users cannot update symptoms
        """
        # hit the API endpoint
        response = self.client.put(
            reverse(ENDPOINT, kwargs={VERSION: API_VERSION_V1}),
            {"name": "test 4", "frequency": 0}
        )

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

