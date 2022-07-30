from rest_framework import serializers
from .models import Restaurant, Menu


# Restaurant serializer
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


# Menu Serializer
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["day", "restaurant", "dishes", "created_at", "modified_at"]
        extra_kwargs = {
            'created_at': {'required': False},
            'modified_at': {'required': False},
        }
