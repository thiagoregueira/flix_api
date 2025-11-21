from django.db.models.aggregates import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated

from movies.models import Movie
from reviews.models import Review
from movies.serializers import MovieModelSerializer, MovieListDetailSerializer
from app.permissions import GlobalPermission


class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalPermission]
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalPermission]
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieStatsView(views.APIView):
    permission_classes = [IsAuthenticated, GlobalPermission]
    queryset = Movie.objects.all()

    def get(self, request):
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        geral_average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        return response.Response(
            data={
                'total_movies': total_movies,
                'movies_by_genre': movies_by_genre,
                'total_reviews': total_reviews,
                'general_average_stars': round(geral_average_stars, 1) if geral_average_stars else 0,
            },
            status=status.HTTP_200_OK,
        )
