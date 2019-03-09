"""
Tests for Diagnosis View
"""
from django.urls import reverse
from rest_framework import status
from tortuga.apps.diagnoses.models import Diagnosis
from tortuga.apps.diagnoses.serializer import DiagnosisSerializer
from tortuga.apps.diagnoses.__tests__.base import BaseViewTest, API_VERSION_V1, VERSION, SID


ENDPOINT = "diagnoses-all"


class DiagnosesViewTest(BaseViewTest):
    """
    Tests for getting all diagnoses
    """
    def test_get_all_diagnoses(self):
        """
        This test ensures that all diagnoses added in the setUp method
        exist when we make a GET request to the symptoms/:id/diagnoses/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse(ENDPOINT, kwargs={VERSION: API_VERSION_V1, SID: self.valid_symptom_id})
        )
        # fetch the data from db
        expected = Diagnosis.objects.all()
        serialized = DiagnosisSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_diagnoses_alt(self):
        """
        Returns an empty list of diagnoses
        """
        # hit the API endpoint
        response = self.client.get(
            reverse(ENDPOINT, kwargs={VERSION: API_VERSION_V1, SID: 100})
        )
        # fetch the data from db
        expected = []
        serialized = DiagnosisSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_diagnoses_custom(self):
        """
        Returns only a subset of the diagnoses matching the id
        """
        symptom1 = BaseViewTest.create_symptom("sore-throat")
        symptom2 = BaseViewTest.create_symptom("itchy-rash")
        diagnosis1 = BaseViewTest.create_diagnosis(symptom1, "strep throat")
        BaseViewTest.create_diagnosis(symptom2, "hives")
        # hit the API endpoint
        response = self.client.get(
            reverse(ENDPOINT, kwargs={VERSION: API_VERSION_V1, SID: symptom1.id})
        )
        # fetch the data from db
        expected = [diagnosis1]
        serialized = DiagnosisSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
