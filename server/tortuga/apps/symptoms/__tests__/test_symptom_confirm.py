"""
Tests for Symptom Confirm
"""
from django.urls import reverse
from rest_framework import status
from tortuga.apps.symptoms.models import Symptom
from tortuga.apps.symptoms.serializer import SymptomSerializer
from tortuga.apps.symptoms.__tests__.base import BaseViewTest, API_VERSION_V1, VERSION

ID = "id"
ENDPOINT = "symptom-confirm"


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
            reverse(ENDPOINT, kwargs={VERSION: API_VERSION_V1, ID: self.valid_symptom_id})
        )

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_create_symptom(self):
        """
        This test ensures users cannot create new symptoms
        """
        # hit the API endpoint
        response = self.client.post(
            reverse(ENDPOINT, kwargs={VERSION: API_VERSION_V1, ID: self.valid_symptom_id})
        )

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_symptom(self):
        """
        This test ensures users cannot delete symptoms
        """
        # hit the API endpoint
        response = self.client.post(
            reverse(ENDPOINT, kwargs={VERSION: API_VERSION_V1, ID: self.valid_symptom_id})
        )

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_symptom(self):
        """
        This test ensures that frequency is updated
        """
        # hit the API endpoint
        target = Symptom.objects.get(id=self.valid_symptom_id)
        target.frequency += 1
        response = self.client.put(
            reverse(
                ENDPOINT,
                kwargs={VERSION: API_VERSION_V1, ID: self.valid_symptom_id},
            ),
            content_type='application/json'
        )
        # fetch the data from db
        serialized = SymptomSerializer(target)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_symptom_alt(self):
        """
        This test ensures users cannot update symptoms
        """
        # hit the API endpoint
        target = Symptom.objects.get(id=self.valid_symptom_id_alt)
        target.frequency += 1
        response = self.client.put(
            reverse(
                ENDPOINT,
                kwargs={VERSION: API_VERSION_V1, ID: self.valid_symptom_id_alt},
            ),
            content_type='application/json'
        )
        # fetch the data from db
        serialized = SymptomSerializer(target)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
