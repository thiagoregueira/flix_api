from django.urls import path
from .views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
)


urlpatterns = [
    path('authentication/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authentication/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('authentication/token/verify/', CustomTokenVerifyView.as_view(), name='token_verify'),
]
