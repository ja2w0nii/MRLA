from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from users.models import User
from users.serializers import UserSerializer, ProfileSerializer, ProfileUpdateSerializer, FollowSerializer


# 회원 가입/탈퇴
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = get_object_or_404(User, id=request.user.id)
        if user:
            user.delete()
            return Response({"message": "지금까지 저희 서비스를 이용해 주셔서 감사합니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "이런... 탈퇴에 실패하셨습니다."}, status=status.HTTP_400_BAD_REQUEST)


# 프로필 조회/수정
class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        profile = User.objects.get(id=request.user.id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        profile = User.objects.get(id=request.user.id)
        serializer = ProfileUpdateSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# 팔로잉 등록/취소
class DoFollowView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if request.user in user.follower.all():
            user.follower.remove(request.user)
            return Response("팔로우 취소", status=status.HTTP_200_OK)
        else:
            user.follower.add(request.user)
            return Response("팔로우 완료", status=status.HTTP_200_OK)
        

# 팔로잉/팔로워 리스트 보기
class FollowView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        following = get_object_or_404(User, id=request.user.id)
        serializer = FollowSerializer(following)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
