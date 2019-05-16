"""
Diagnosis serializer
"""

from rest_framework import serializers
from tortuga.apps.diagnoses.models import Diagnosis


class DiagnosisSerializer(serializers.ModelSerializer):
    """
    Diagnosis serializer
    """
    class Meta:
        """
        Meta information about the diagnosis model
        """
        model = Diagnosis
        fields = ("id", "name", "frequency")
