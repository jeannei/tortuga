"""
API endpoints for Diagnosis
"""

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from tortuga.apps.diagnoses.models import Diagnosis
from tortuga.apps.diagnoses.serializer import DiagnosisSerializer


class DiagnosesView(generics.ListAPIView):
    """
    GET symptoms/:sid/diagnoses
    """
    serializer_class = DiagnosisSerializer

    def get_queryset(self):
        """
        Return all diagnoses that match the provide SID (symptom id)
        """
        sid = self.kwargs["sid"]
        return Diagnosis.objects.filter(symptom_id=sid)


class DiagnosisConfirmView(generics.UpdateAPIView):
    """
    PUT symptoms/:sid/diagnoses/:id/confirm
    """
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer

    def put(self, request, *args, **kwargs):
        """
        Update target symptom frequency
        """
        sid = kwargs["sid"]
        primary_key = kwargs["id"]
        try:
            current_diagnosis = self.queryset.get(pk=primary_key)
            if current_diagnosis.symptom_id != sid:
                return self.error_response(
                    status.HTTP_400_BAD_REQUEST,
                    "Invalid symptom id: {}".format(sid)
                )

            serializer = DiagnosisSerializer()
            updated_diagnosis = serializer.update(
                current_diagnosis,
                {"frequency": current_diagnosis.frequency + 1}
            )
            return Response(DiagnosisSerializer(updated_diagnosis).data)
        except Diagnosis.DoesNotExist:
            return self.error_response(
                status.HTTP_404_NOT_FOUND,
                "Diagnosis with id: {} does not exist".format(primary_key)
            )

    @staticmethod
    def error_response(http_status, message):
        return Response(
            data={"message": message},
            status=http_status
        )
