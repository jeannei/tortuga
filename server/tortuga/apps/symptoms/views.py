"""
API endpoints for Symptoms
"""

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from tortuga.apps.symptoms.models import Symptom
from tortuga.apps.symptoms.serializer import SymptomSerializer


class SymptomsView(generics.ListAPIView):
    """
    GET symptoms
    """
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer


class SymptomView(generics.RetrieveAPIView):
    """
    GET symptoms/:id
    """
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer

    def get(self, request, *args, **kwargs):
        """
        Get symptom by id or not found
        """
        primary_key = kwargs["id"]
        try:
            symptom = self.queryset.get(pk=primary_key)
            return Response(SymptomSerializer(symptom).data)
        except Symptom.DoesNotExist:
            return Response(
                data={"message": "Symptom with id: {} does not exist".format(primary_key)},
                status=status.HTTP_404_NOT_FOUND
            )


class SymptomConfirmView(generics.UpdateAPIView):
    """
    PUT symptoms/:id/confirm
    """
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer

    def put(self, request, *args, **kwargs):
        """
        Update target symptom frequency
        """
        primary_key = kwargs["id"]
        try:
            current_symptom = self.queryset.get(pk=primary_key)
            serializer = SymptomSerializer()
            updated_symptom = serializer.update(
                current_symptom,
                {"frequency": current_symptom.frequency + 1}
            )
            return Response(SymptomSerializer(updated_symptom).data)
        except Symptom.DoesNotExist:
            return Response(
                data={"message": "Symptom with id: {} does not exist".format(primary_key)},
                status=status.HTTP_404_NOT_FOUND
            )
