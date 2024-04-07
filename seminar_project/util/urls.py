from django.contrib import admin
from django.urls import path

from util import views

urlpatterns = [
    path('', views.health),
]
