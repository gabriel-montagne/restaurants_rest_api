from rest_framework import serializers

from . import models

class RestaurantItemSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items."""

    class Meta:
        model = models.RestaurantItem
        fields = ('id', 'name', 'opens_at', 'closes_at')
