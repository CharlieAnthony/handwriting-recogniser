from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from . import views
# from ..config.urls import urlpatterns


urlpatterns = [
    path('', views.mainPage, name="main")
]
