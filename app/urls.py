from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('authentication.urls'), name='authentication-api'),
    path('api/v1/', include('genres.urls'), name='genres-api'),
    path('api/v1/', include('actors.urls'), name='actors-api'),
    path('api/v1/', include('movies.urls'), name='movies-api'),
    path('api/v1/', include('reviews.urls'), name='reviews-api'),
]
