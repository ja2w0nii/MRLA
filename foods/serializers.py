from rest_framework import serializers
from foods.models import Food, FoodComment


# 메뉴 리스트
class FoodSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()

    def get_likes(self, obj):
        return obj.likes.count()

    class Meta:
        model = Food
        fields = "__all__"


# 추천 메뉴 리스트
class FilteringFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ("food_id", "menu", "image", "major_category")

        
class FoodCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodComment
        fields = "__all__"

        
class FoodCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodComment
        fields = ("menu_id", "menu", "comment")
