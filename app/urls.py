from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from app.renderers import CustomOpenApiRenderer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('authentication.urls'), name='authentication-api'),
    path('api/v1/', include('genres.urls'), name='genres-api'),
    path('api/v1/', include('actors.urls'), name='actors-api'),
    path('api/v1/', include('movies.urls'), name='movies-api'),
    path('api/v1/', include('reviews.urls'), name='reviews-api'),
    path(
        'api/schema/',
        SpectacularAPIView.as_view(renderer_classes=[CustomOpenApiRenderer]),
        name='schema',
    ),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
