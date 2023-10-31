from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from users import views


urlpatterns = [
    path("signup/", views.UserView.as_view(), name="user_view"),
    path("myprofile/", views.MyProfileView.as_view(), name="my_profile_view"),
    path("profile/<int:user_id>/", views.ProfileView.as_view(), name="profile_view"),
    path("follow/<int:user_id>/", views.FollowView.as_view(), name="follow_view"),
    path("following/<int:user_id>/", views.FollowingView.as_view(), name="following_view"),
    path("follower/<int:user_id>/", views.FollowerView.as_view(), name="follower_view"),
    path("api/token/", views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("kakao/login/", views.kakao_login, name="kakao_login"),
    path("kakao/callback/", views.kakao_View.as_view(), name="kakao_callback"),
    path("kakao/login/finish/", views.KakaoLogin.as_view(), name="kakao_login_todjango"),
    path("", include("allauth.urls")),
]
