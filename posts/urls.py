from django.urls import path
from posts import views

urlpatterns = [
    path("service/", views.ServiceView.as_view(), name="service_view"),
    path("service/<int:service_id>/", views.ServiceDetailtView.as_view(), name="service_detail_view"),
    path("service/<int:service_id>/comment/", views.ServiceCommentView.as_view(), name="service_comment_view"),
]
