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
        pk = kwargs["id"]
        try:
            a_symptom = self.queryset.get(pk=pk)
            return Response(SymptomSerializer(a_symptom).data)
        except Symptom.DoesNotExist:
            return Response(
                data={"message": "Symptom with id: {} does not exist".format(pk)},
                status=status.HTTP_404_NOT_FOUND
            )
