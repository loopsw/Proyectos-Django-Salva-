from django.contrib import admin
from django.urls import path

from sendemail.views import contactView, successView

urlpatterns = [
    path('contact/',contactView,name="contacto"),
    path('success/',successView,name="success"),
]
