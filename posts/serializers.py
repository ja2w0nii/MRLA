from rest_framework import serializers
from posts.models import Service, ServiceComment


# 고객센터 게시글 조회
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("id", "title", "created_at")


# 고객센터 게시글 등록
class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("title", "content")


# 고객센터 게시글 댓글 조회
class ServiceCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceComment
        fields = ("service", "comment", "created_at", "updated_at")


# 고객센터 게시글 댓글 등록
class ServiceCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceComment
        fields = ("comment",)
