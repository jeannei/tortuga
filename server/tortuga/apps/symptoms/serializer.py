"""
Symptom serializer
"""

from rest_framework import serializers
from tortuga.apps.symptoms.models import Symptom


class SymptomSerializer(serializers.ModelSerializer):
    """
    Symptom serializer
    """
    class Meta:
        """
        Meta information about the diagnosis model
        """
        model = Symptom
        fields = ("id", "name", "frequency")
