"""
Symptom resources
"""

from django.urls import path
from tortuga.apps.symptoms.views import SymptomView

# this constant must be lowercase for django to work correctly, so we tell pylint to ignore it
# pylint: disable=C0103
urlpatterns = [
    path('symptoms/', SymptomView.as_view(), name="symptoms-all")
]
