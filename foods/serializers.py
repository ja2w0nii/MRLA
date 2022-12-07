from rest_framework import serializers
from foods.models import Food


# 메뉴 리스트
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


# 추천 메뉴 리스트
class FilteringFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ("food_id", "menu", "image")
