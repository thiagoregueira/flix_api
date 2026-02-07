from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(
    post=extend_schema(summary='Obter token JWT (Login)', tags=['Autenticação']),
)
class CustomTokenObtainPairView(TokenObtainPairView):
    pass


@extend_schema_view(
    post=extend_schema(summary='Atualizar token JWT', tags=['Autenticação']),
)
class CustomTokenRefreshView(TokenRefreshView):
    pass


@extend_schema_view(
    post=extend_schema(summary='Verificar validade do token JWT', tags=['Autenticação']),
)
class CustomTokenVerifyView(TokenVerifyView):
    pass
