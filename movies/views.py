from django.db.models.aggregates import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema_view, extend_schema

from movies.models import Movie
from reviews.models import Review
from movies.serializers import MovieModelSerializer, MovieListDetailSerializer
from app.permissions import GlobalPermission


@extend_schema_view(
    get=extend_schema(summary='Listar os filmes', tags=['Filmes']),
    post=extend_schema(summary='Criar novo filme', tags=['Filmes']),
)
class MovieListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalPermission]
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer


@extend_schema_view(
    get=extend_schema(summary='Obter detalhes do filme', tags=['Filmes']),
    put=extend_schema(summary='Atualizar dados do filme', tags=['Filmes']),
    patch=extend_schema(summary='Atualizar parcialmente dados do filme', tags=['Filmes']),
    delete=extend_schema(summary='Excluir filme', tags=['Filmes']),
)
class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalPermission]
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer


@extend_schema(summary='Obter estatísticas dos filmes', tags=['Filmes'])
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
