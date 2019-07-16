from rest_framework import routers
from .views import send_otp
from django.urls import path


urlpatterns = [
    path('send-otp', send_otp)
]
