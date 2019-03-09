"""
tortuga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path, re_path
from rest_framework.documentation import include_docs_urls

# this constant must be lowercase for django to work correctly, so we tell pylint to ignore it
# pylint: disable=C0103
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='Tortuga API')),
    re_path('(?P<version>(v1))/', include('tortuga.apps.symptoms.urls')),
    re_path('(?P<version>(v1))/', include('tortuga.apps.diagnoses.urls'))
]
