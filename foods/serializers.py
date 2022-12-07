from rest_framework import serializers
from foods.models import Food, FoodComment


# 메뉴 리스트
class FoodSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()

    def get_likes(self, obj):
        return obj.likes.count()
    

class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = "__all__"



# 추천 메뉴 리스트
class FilteringFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ("food_id", "menu", "image")

class FoodCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodComment
        fields = ("food", "comment", "created_at", "updated_at")

class FoodCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodComment
        fields = ("comment",)

