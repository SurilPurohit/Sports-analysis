from django.contrib import admin
from django.urls import path,include
from .views import foot

urlpatterns = [
    path('', foot, name = 'football'),
]