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
    GET diagnoses
    """
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer
