from django.urls import path,include
from .views import upcom

urlpatterns = [
    path('', upcom, name = 'upcoming'),
]