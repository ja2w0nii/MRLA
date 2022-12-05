from rest_framework import serializers
from foods.models import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class FilteringFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ("menu", "image")