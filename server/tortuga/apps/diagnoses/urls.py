"""
Diagnosis resources
"""

from django.urls import path
from tortuga.apps.diagnoses.views import DiagnosesView, DiagnosisConfirmView

# this constant must be lowercase for django to work correctly, so we tell pylint to ignore it
# pylint: disable=C0103
urlpatterns = [
    path('symptoms/<int:sid>/diagnoses', DiagnosesView.as_view(), name="diagnoses-all"),
    path(
        'symptoms/<int:sid>/diagnoses/<int:id>/confirm',
        DiagnosisConfirmView.as_view(),
        name="diagnosis-confirm"
    )
]
