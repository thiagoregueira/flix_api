# import json
# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema_view, extend_schema

from genres.models import Genre
from genres.serializers import GenreSerializer
from app.permissions import GlobalPermission


@extend_schema_view(
    get=extend_schema(summary='Listar os gêneros', tags=['Gêneros']),
    post=extend_schema(summary='Criar novo gênero', tags=['Gêneros']),
)
class GenreListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalPermission]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


@extend_schema_view(
    get=extend_schema(summary='Obter detalhes do gênero', tags=['Gêneros']),
    put=extend_schema(summary='Atualizar dados do gênero', tags=['Gêneros']),
    patch=extend_schema(summary='Atualizar parcialmente dados do gênero', tags=['Gêneros']),
    delete=extend_schema(summary='Excluir gênero', tags=['Gêneros']),
)
class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalPermission]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# Usando Apenas Django (Function Based Views)
# @csrf_exempt
# def genre_create_list_view(request):
#     if request.method == 'GET':
#         genres = Genre.objects.all()
#         data = [
#             {
#                 'id': genre.id,
#                 'name': genre.name,
#             }
#             for genre in genres
#         ]
#         return JsonResponse(data, safe=False)

#     elif request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))
#         new_genre = Genre(name=data['name'])
#         new_genre.save()
#         return JsonResponse(
#             {
#                 'id': new_genre.id,
#                 'name': new_genre.name,
#             },
#             status=201,
#         )


# @csrf_exempt
# def genre_detail_update_view(request, pk):
#     genre = get_object_or_404(Genre, pk=pk)

#     if request.method == 'GET':
#         data = {
#             'id': genre.id,
#             'name': genre.name,
#         }

#         return JsonResponse(data)

#     elif request.method == 'PUT':
#         data = json.loads(request.body.decode('utf-8'))
#         genre.name = data['name']
#         genre.save()
#         return JsonResponse(
#             {
#                 'id': genre.id,
#                 'name': genre.name,
#             },
#             status=200,
#         )

#     elif request.method == 'DELETE':
#         genre.delete()
#         return JsonResponse(
#             {
#                 'message': 'Gênero excluído com sucesso!',
#             },
#             status=204,
#         )
