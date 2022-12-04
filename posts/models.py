from django.db import models
from users.models import User


class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="service_user")
    title = models.CharField(verbose_name="고객센터 게시글 제목", max_length=50)
    content = models.TextField(verbose_name="고객센터 게시글 내용")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f"{self.user} / {self.title}")


class ServiceComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="servicecomment_user")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="servicecomment_service")
    comment = models.TextField(verbose_name="고객센터 게시글 댓글 내용(운영진 전용)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(f"{self.service} / {self.comment}")
