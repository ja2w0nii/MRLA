from django.urls import path
from posts import views

urlpatterns = [
    path("service/", views.ServiceView.as_view(), name="service_view"),
    path("service/<int:service_id>/", views.ServiceCommentView.as_view(), name="service_comment_view"),
    path("community/", views.CommunityView.as_view(), name="community_view"),
    path('community/<int:community_id>/',views.CommunityDetailView.as_view(), name='community_detail_view'),
    path('community/<int:community_id>/comment/',views.CommunityCommentView.as_view(), name='community_comment_view'),
    path('community/<int:community_id>/comment/<int:comment_id>/',views.CommunityCommentDetailView.as_view(), name='community_comment_Detail_view'),
]
