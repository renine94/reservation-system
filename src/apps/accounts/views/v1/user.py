from drf_yasg.utils import swagger_auto_schema

from src.apps.accounts.models import User
from src.apps.accounts.serializers.v1.user import UserSerializer, TokenSerializer

from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError

from src.apps.accounts.permissions import IsOwnerOnly


class UserCRUDView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()

    def get_authenticators(self):
        """회원 탈퇴는 인증 필요"""
        if self.request.method == "DELETE":
            return [JWTAuthentication()]
        if any([p in self.request.path for p in ["logout", "me"]]):
            return [JWTAuthentication()]
        return [auth() for auth in self.authentication_classes]

    def get_permissions(self):
        """삭제는 staff 거나 나 자신만"""
        if self.action in ["destroy", "me"]:
            return [IsOwnerOnly()]
        if self.action == "logout":
            return [IsAuthenticated()]
        return [permission() for permission in self.permission_classes]

    @swagger_auto_schema(operation_summary="회원 가입 API")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        password = serializer.validated_data.pop("password2")
        serializer.validated_data["password"] = make_password(password)
        super().perform_create(serializer)

    def perform_destroy(self, instance: User) -> None:
        """회원탈퇴 오버라이딩, 실제 DB삭제처리 않고 soft-delete 처리"""
        instance.is_active = False
        instance.save()

    @swagger_auto_schema(
        request_body=TokenObtainPairSerializer, responses={200: TokenSerializer}, operation_summary="유저 로그인"
    )
    def login(self, request):
        """email과 password로 로그인하여 access, refresh 토큰을 발행한다."""
        serializer = TokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    def login_refresh(self, request):
        """로그인 갱신"""
        serializer = TokenRefreshSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=["post"],
        authentication_classes=(JWTAuthentication,),
        permission_classes=(IsAuthenticated,),
    )
    def logout(self, request):
        """로그아웃 (refresh token 차단)"""
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "logout success!"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def me(self, request):
        """내 정보 보기, 토큰으로 요청 보낸 상태이어야 합니다."""
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
