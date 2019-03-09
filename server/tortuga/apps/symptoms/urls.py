"""
Symptom resources
"""

from django.urls import path
from tortuga.apps.symptoms.views import SymptomsView, SymptomView

# this constant must be lowercase for django to work correctly, so we tell pylint to ignore it
# pylint: disable=C0103
urlpatterns = [
    path('symptoms', SymptomsView.as_view(), name="symptoms-all"),
    path('symptoms/<int:id>', SymptomView.as_view(), name="symptom-detail")
]
