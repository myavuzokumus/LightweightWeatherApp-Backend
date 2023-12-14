from django.urls import path
from .views import GooglePlacesAPI

urlpatterns = [
    path('places', GooglePlacesAPI, name='GooglePlacesAPI'),
]