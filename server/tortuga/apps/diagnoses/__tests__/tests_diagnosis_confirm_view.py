"""
Tests for Diagnosis Confirm View
"""
from django.urls import reverse
from rest_framework import status
from tortuga.apps.diagnoses.models import Diagnosis
from tortuga.apps.diagnoses.serializer import DiagnosisSerializer
from tortuga.apps.diagnoses.__tests__.base import BaseViewTest, API_VERSION_V1, VERSION, SID


ENDPOINT = "diagnosis-confirm"
ID = "id"


class DiagnosisConfirmViewTest(BaseViewTest):
    """
    Tests for confirming a diagnoses
    """
    def test_get_diagnosis_by_id(self):
        """
        This test ensures that get function is not supported
        """
        # hit the API endpoint
        response = self.client.get(
            reverse(
                ENDPOINT,
                kwargs={
                    VERSION: API_VERSION_V1,
                    SID: self.valid_symptom_id,
                    ID: self.valid_diagnosis_id
                },
            ),
            content_type='application/json'
        )
        # fetch the data from db
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_diagnosis_by_id(self):
        """
        This test ensures that delete function is not supported
        """
        # hit the API endpoint
        response = self.client.delete(
            reverse(
                ENDPOINT,
                kwargs={
                    VERSION: API_VERSION_V1,
                    SID: self.valid_symptom_id,
                    ID: self.valid_diagnosis_id
                },
            ),
            content_type='application/json'
        )
        # fetch the data from db
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_post_diagnosis_by_id(self):
        """
        This test ensures that post function is not supported
        """
        # hit the API endpoint
        response = self.client.post(
            reverse(
                ENDPOINT,
                kwargs={
                    VERSION: API_VERSION_V1,
                    SID: self.valid_symptom_id,
                    ID: self.valid_diagnosis_id
                },
            ),
            content_type='application/json'
        )
        # fetch the data from db
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_diagnosis(self):
        """
        This test ensures that frequency is updated
        """
        # hit the API endpoint
        target = Diagnosis.objects.get(id=self.valid_diagnosis_id)
        target.frequency += 1
        response = self.client.put(
            reverse(
                ENDPOINT,
                kwargs={VERSION: API_VERSION_V1, SID: self.valid_symptom_id, ID: self.valid_diagnosis_id},
            ),
            content_type='application/json'
        )
        # fetch the data from db
        serialized = DiagnosisSerializer(target)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_diagnosis_alt(self):
        """
        This test ensures that frequency is updated using alternate id
        """
        # hit the API endpoint
        target = Diagnosis.objects.get(id=self.valid_diagnosis_id_alt)
        target.frequency += 1
        response = self.client.put(
            reverse(
                ENDPOINT,
                kwargs={
                    VERSION: API_VERSION_V1,
                    SID: self.valid_symptom_id,
                    ID: self.valid_diagnosis_id_alt
                },
            ),
            content_type='application/json'
        )
        # fetch the data from db
        serialized = DiagnosisSerializer(target)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_diagnosis_invalid_symptom_id(self):
        """
        This test ensures a bad request is sent when using invalid symptom id
        """
        # hit the API endpoint
        response = self.client.put(
            reverse(
                ENDPOINT,
                kwargs={
                    VERSION: API_VERSION_V1,
                    SID: self.invalid_symptom_id,
                    ID: self.valid_diagnosis_id_alt
                },
            ),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_diagnosis_invalid_diagnosis_id(self):
        """
        This test ensures that frequency is updated using alternate id
        """
        # hit the API endpoint
        response = self.client.put(
            reverse(
                ENDPOINT,
                kwargs={
                    VERSION: API_VERSION_V1,
                    SID: self.valid_symptom_id,
                    ID: self.invalid_diagnosis_id
                },
            ),
            content_type='application/json'
        )
        # fetch the data from db
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
