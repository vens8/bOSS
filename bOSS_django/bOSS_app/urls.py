from django.urls import path
from bOSS_app.views import *
from . import views
from django.conf import settings

urlpatterns = [
    path('', home),
]