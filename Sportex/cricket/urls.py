from django.contrib import admin
from django.urls import path,include
from .views import cric

urlpatterns = [
    path('', cric, name = 'cricket'),
]