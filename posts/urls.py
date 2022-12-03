from django.urls import path
from posts import views

urlpatterns = [
    path("service/", views.ServiceView.as_view(), name="service_view"),
    path("service/<int:service_id>/", views.ServiceCommentView.as_view(), name="service_comment_view"),
]
