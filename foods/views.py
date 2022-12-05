from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from foods.models import Food
from foods.serializers import FoodSerializer, FilteringFoodSerializer
from foods.collaborative_filtering import collaborative_filtering
# from django.core import serializers
# from django.http import HttpResponse


# 음식 리스트 조회
class FoodList(APIView):
    def get(self, request):
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 음식에 대한 좋아요 리스트
# class FoodLikeView(APIView):
#     def get(self, request):
#         food_like = FoodLike.objects.filter(id__isnull=False).order_by("user_id")
#         food_like_list = serializers.serialize('json', food_like)
#         return HttpResponse(food_like_list, content_type="text/json-comment-filtered")


# 추천 음식 리스트 조회
class FilteringFoodView(APIView):
    def get(self, request, user_id):
        food_list = []
        foods = collaborative_filtering(request, user_id)
        for food in foods:
            recommend_food = get_object_or_404(Food, food_id=food)
            food_list.append(recommend_food)
        serializer = FilteringFoodSerializer(food_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
