from rest_framework import serializers
from foods.models import Food, FoodComment



class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class FoodCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodComment
        fields = ("food", "comment", "created_at", "updated_at")

class FoodCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodComment
        fields = ("comment",)
