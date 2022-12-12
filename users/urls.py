from django.urls import path
from users import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [

    path("signup/", views.UserView.as_view(), name="user_view"),
    path("profile/", views.ProfileView.as_view(), name="profile_view"),
    path("follow/", views.FollowView.as_view(), name="follow_view"),
    path("follow/<int:user_id>/", views.DoFollowView.as_view(), name="do_follow_view"),

    path('kakao/login/', views.kakao_login, name='kakao_login'),
    path('kakao/callback/', views.kakao_View.as_view(), name='kakao_callback'),
    path('kakao/login/finish/', views.KakaoLogin.as_view(), name='kakao_login_todjango'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("signup/", views.UserView.as_view(), name="user_view"),
    path("profile/", views.ProfileView.as_view(), name="profile_view"),

    # path('google/login/', views.google_login, name='google_login'),
    # path('google/callback/', views.google_callback, name='google_callback'),
    # path('google/login/finish/', views.GoogleLogin.as_view(), name='google_login_todjango'),


]
