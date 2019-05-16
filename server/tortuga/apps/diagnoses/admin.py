"""
Register diagnosis for admin usage
"""

from django.contrib import admin
from tortuga.apps.diagnoses.models import Diagnosis

admin.site.register(Diagnosis)
