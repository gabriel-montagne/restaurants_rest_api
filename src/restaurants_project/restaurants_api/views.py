from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from . import models

# Create your views here.

class RestaurantItemViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating and deleting restaurant items."""

    serializer_class = serializers.RestaurantItemSerializer
    queryset = models.RestaurantItem.objects.all()
