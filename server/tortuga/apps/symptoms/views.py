"""
API endpoints for Symptoms
"""

from rest_framework import generics
from tortuga.apps.symptoms.models import Symptom
from tortuga.apps.symptoms.serializer import SymptomSerializer


class SymptomView(generics.ListCreateAPIView):
    """
    API endpoints for Symptoms
    """
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer
