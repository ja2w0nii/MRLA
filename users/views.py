from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView
import os
import requests
from json import JSONDecodeError
from django.http import JsonResponse
from django.shortcuts import redirect, render
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.google import views as google_view
from allauth.socialaccount.providers.kakao import views as kakao_view
from users.models import User
from users.serializers import (
    CustomTokenObtainPairSerializer,
    UserSerializer,
    ProfileSerializer,
    ProfileUpdateSerializer,
    FollowSerializer,
)


# 회원 가입/탈퇴
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = get_object_or_404(User, id=request.user.id)
        if user:
            user.delete()
            return Response(
                {"message": "지금까지 저희 서비스를 이용해 주셔서 감사합니다."}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": "이런... 탈퇴에 실패하셨습니다."}, status=status.HTTP_400_BAD_REQUEST
            )


# 로그인한 유저의 프로필 정보 조회
class MyProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        profile = get_object_or_404(User, id=request.user.id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# 프로필 조회/수정
class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        profile = get_object_or_404(User, id=user_id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id):
        profile = get_object_or_404(User, id=user_id)
        serializer = ProfileUpdateSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 팔로우 등록/취소
class FollowView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if request.user in user.follower.all():
            user.follower.remove(request.user)
            return Response({"message": "팔로우 취소"}, status=status.HTTP_200_OK)
        else:
            user.follower.add(request.user)
            return Response({"message": "팔로우 완료"}, status=status.HTTP_200_OK)


# 팔로잉 목록 조회
class FollowingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        following = user.following.all()
        serializer = FollowSerializer(following, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 팔로워 목록 조회
class FollowerView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        follower = user.follower.all()
        serializer = FollowSerializer(follower, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# 소셜 로그인
BASE_URL = "https://mechurial.mrla.tk/"
KAKAO_CALLBACK_URI = BASE_URL + "signin_signup.html"


def kakao_login(request):
    rest_api_key = os.environ.get("KAKAO_REST_API_KEY")
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={rest_api_key}&redirect_uri={KAKAO_CALLBACK_URI}&response_type=code"
    )


class kakao_View(APIView):
    def post(self, request):
        rest_api_key = os.environ.get("KAKAO_REST_API_KEY")
        code = request.data.get("code")
        print(code)
        redirect_uri = KAKAO_CALLBACK_URI
        """
        Access Token Request
        """
        token_req = requests.post(
            f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={rest_api_key}&redirect_uri={redirect_uri}&code={code}"
        )
        token_req_json = token_req.json()
        error = token_req_json.get("error")
        if error is not None:
            raise JSONDecodeError(error)
        access_token = token_req_json.get("access_token")
        print(access_token)
        """
        Email Request
        """
        profile_request = requests.post(
            "https://kapi.kakao.com/v2/user/me",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        profile_json = profile_request.json()

        kakao_account = profile_json.get("kakao_account")
        print(profile_json)

        """
        kakao_account에서 이메일 외에
        카카오톡 프로필 이미지, 배경 이미지 url 가져올 수 있음
        print(kakao_account) 참고
        """
        # print(kakao_account)
        email = kakao_account.get("email")
        """
        Signup or Signin Request
        """
        try:
            user = User.objects.get(email=email)
            # 기존에 가입된 유저의 Provider가 kakao가 아니면 에러 발생, 맞으면 로그인
            # 다른 SNS로 가입된 유저
            social_user = SocialAccount.objects.get(user=user)
            if social_user is None:
                return JsonResponse(
                    {"err_msg": "email exists but not social user"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            if social_user.provider != "kakao":
                return JsonResponse(
                    {"err_msg": "no matching social type"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # 기존에 Google로 가입된 유저

            data = {"access_token": access_token, "code": code}
            accept = requests.post(
                "https://www.mrla.tk/users/kakao/login/finish/", data=data
            )

            print(accept)
            accept_status = accept.status_code
            if accept_status != 200:
                return JsonResponse(
                    {"err_msg": "failed to signin"}, status=accept_status
                )
            accept_json = accept.json()
            accept_json.pop("user", None)
            return JsonResponse(accept_json)
        except User.DoesNotExist:
            # 기존에 가입된 유저가 없으면 새로 가입

            data = {"access_token": access_token, "code": code}
            accept = requests.post(
                "https://www.mrla.tk/users/kakao/login/finish/", data=data
            )

            accept_status = accept.status_code
            if accept_status != 200:
                return JsonResponse(
                    {"err_msg": "failed to signup"}, status=accept_status
                )
            # user의 pk, email, first name, last name과 Access Token, Refresh token 가져옴
            accept_json = accept.json()
            accept_json.pop("user", None)
            return JsonResponse(accept_json)


class KakaoLogin(SocialLoginView):
    adapter_class = kakao_view.KakaoOAuth2Adapter
    client_class = OAuth2Client
    callback_url = KAKAO_CALLBACK_URI


def index(request):
    print(request.user.is_authenticated)

    return render(request, "coplate/index.html")
