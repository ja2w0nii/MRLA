from rest_framework import permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import Service
from posts.serializers import ServiceSerializer, ServiceCreateSerializer, ServiceCommentSerializer, ServiceCommentCreateSerializer


# 고객센터 게시글 조회/등록
class ServiceView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        posts = Service.objects.all().order_by("-id")
        serializer = ServiceSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request):
        serializer = ServiceCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 고객센터 게시글 댓글 조회/등록
class ServiceCommentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, service_id):
        service = get_object_or_404(Service, id=service_id)
        comments = service.servicecomment_service.all()
        if request.user == service.user or request.user.is_admin:
            serializer = ServiceCommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "권한이 없습니다!"}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, service_id):
        serializer = ServiceCommentCreateSerializer(data=request.data)
        if request.user.is_admin:
            if serializer.is_valid():
                serializer.save(user=request.user, service_id=service_id)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "권한이 없습니다!"}, status=status.HTTP_401_UNAUTHORIZED)
