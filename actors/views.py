from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema_view, extend_schema

from actors.models import Actor
from actors.serializers import ActorSerializer
from app.permissions import GlobalPermission


@extend_schema_view(
    get=extend_schema(summary='Listar os atores', tags=['Atores']),
    post=extend_schema(summary='Criar novo ator', tags=['Atores']),
)
class ActorListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalPermission]
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


@extend_schema_view(
    get=extend_schema(summary='Obter detalhes do ator', tags=['Atores']),
    put=extend_schema(summary='Atualizar dados do ator', tags=['Atores']),
    patch=extend_schema(summary='Atualizar parcialmente dados do ator', tags=['Atores']),
    delete=extend_schema(summary='Excluir ator', tags=['Atores']),
)
class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalPermission]
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
