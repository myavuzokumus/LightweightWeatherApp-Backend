"""
URL configuration for WeatherAppBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from django.views.static import serve
import os
from api import views

router = routers.DefaultRouter(trailing_slash=False)
router.register('weather-info', views.WeatherInfoAPI)

handler404 = 'WeatherAppBackend.views.error404'

FLUTTER_BASE_DIR = os.path.dirname(os.path.dirname (os.path.abspath (__file__)))
FLUTTER_WEB_APP = os.path.join(FLUTTER_BASE_DIR, 'flutter_web_app')

def flutter_redirect(request, resource):
  return serve(request, resource, FLUTTER_WEB_APP)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    path('api/', include("placesapi.urls")),

    path('', lambda r: flutter_redirect(r, 'index.html')),
    path('<path:resource>', flutter_redirect),
]
