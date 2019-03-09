"""
Tests for Symptom Detail
"""
from django.urls import reverse
from rest_framework import status
from tortuga.apps.symptoms.models import Symptom
from tortuga.apps.symptoms.serializer import SymptomSerializer
from tortuga.apps.symptoms.__tests__.base import BaseViewTest, API_VERSION_V1, VERSION

ID = "id"
SYMPTOM_DETAIL = "symptom-detail"


class SymptomViewTest(BaseViewTest):
    """
    Tests for getting a symptom
    """
    def test_get_symptom(self):
        """
        This tests retrieving a specific symptom
        """
        # hit the API endpoint
        response = self.client.get(
            reverse(SYMPTOM_DETAIL, kwargs={VERSION: API_VERSION_V1, ID: self.valid_symptom_id})
        )
        # fetch the data from db
        expected = Symptom.objects.get(id=self.valid_symptom_id)
        serialized = SymptomSerializer(expected)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_get_symptom(self):
        """
        This tests retrieving an invalid symptom
        """
        # hit the API endpoint
        response = self.client.get(
            reverse(SYMPTOM_DETAIL, kwargs={VERSION: API_VERSION_V1, ID: self.invalid_symptom_id})
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_symptom(self):
        """
        This test ensures users cannot create new symptoms
        """
        # hit the API endpoint
        response = self.client.post(
            reverse(SYMPTOM_DETAIL, kwargs={VERSION: API_VERSION_V1, ID: self.valid_symptom_id})
        )

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_symptom(self):
        """
        This test ensures users cannot delete symptoms
        """
        # hit the API endpoint
        response = self.client.post(
            reverse(SYMPTOM_DETAIL, kwargs={VERSION: API_VERSION_V1, ID: self.valid_symptom_id})
        )

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_symptom(self):
        """
        This test ensures users cannot update symptoms
        """
        # hit the API endpoint
        response = self.client.post(
            reverse(SYMPTOM_DETAIL, kwargs={VERSION: API_VERSION_V1, ID: self.valid_symptom_id})
        )

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

