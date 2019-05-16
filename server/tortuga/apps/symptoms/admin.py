"""
Register symptom for admin usage
"""

from django.contrib import admin
from tortuga.apps.symptoms.models import Symptom

admin.site.register(Symptom)
