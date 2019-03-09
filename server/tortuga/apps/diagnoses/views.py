"""
API endpoints for Diagnosis
"""

from rest_framework import filters, generics
from rest_framework.response import Response
from rest_framework.views import status
from tortuga.apps.diagnoses.models import Diagnosis
from tortuga.apps.diagnoses.serializer import DiagnosisSerializer


class DiagnosesView(generics.ListAPIView):
    """
    GET diagnoses
    """
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer

    def get_queryset(self):
        """
        Return all diagnoses that match the provide SID (symptom id)
        """
        sid = self.kwargs["sid"]
        return Diagnosis.objects.filter(symptom_id=sid)
