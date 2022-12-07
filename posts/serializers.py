from rest_framework import serializers
from posts.models import Service, ServiceComment


# 고객센터 게시글 조회
class ServiceSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Service
        fields = ("id", "user", "title", "created_at")


# 고객센터 게시글 등록
class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("title", "content")


# 고객센터 게시글 디테일 조회
class ServiceDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Service
        fields = ("user", "title", "content", "created_at")


# 고객센터 게시글 디테일 댓글 조회
class ServiceCommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = ServiceComment
        fields = ("user", "service", "comment", "created_at", "updated_at")


# 고객센터 게시글 디테일 댓글 등록
class ServiceCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceComment
        fields = ("comment",)
