from rest_framework import permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from foods.models import Food, FoodComment
from foods.serializers import FoodSerializer, FoodCommentSerializer, FoodCommentCreateSerializer


class FoodView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)     


class FoodCommentView(APIView):

    def get(self, request, food_id):
        food = get_object_or_404(Food, id=food_id)
        comments = food.foodcomment_food.all()
        serializer = FoodCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, food_id):
        serializer = FoodCommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, food_id=food_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, food_id, comment_id):
        comment = get_object_or_404(FoodComment, id=comment_id)
        if request.user == comment.user:
            serializer = FoodCommentCreateSerializer(comment, data=request.data)
            if serializer.is_valid(): 
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "권한이 없습니다!"}, status=status.HTTP_401_UNAUTHORIZED)
    
    def delete(self, request, food_id, comment_id):
        comment = get_object_or_404(FoodComment, id=comment_id)
        if request.user == comment.user:
            comment.delete()
            return Response({"message": "삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "권한이 없습니다!"}, status=status.HTTP_401_UNAUTHORIZED)


# 카테고리별 모아보기는 카테고리가 정리 후 추가구현 예정