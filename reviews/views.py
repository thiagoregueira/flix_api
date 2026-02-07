from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema_view, extend_schema

from reviews.models import Review
from reviews.serializers import ReviewSerializer
from app.permissions import GlobalPermission


@extend_schema_view(
    get=extend_schema(summary='Listar avaliações', tags=['Avaliações']),
    post=extend_schema(summary='Criar nova avaliação', tags=['Avaliações']),
)
class ReviewListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalPermission]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


@extend_schema_view(
    get=extend_schema(summary='Obter detalhes da avaliação', tags=['Avaliações']),
    put=extend_schema(summary='Atualizar avaliação', tags=['Avaliações']),
    patch=extend_schema(summary='Atualizar parcialmente avaliação', tags=['Avaliações']),
    delete=extend_schema(summary='Excluir avaliação', tags=['Avaliações']),
)
class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalPermission]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
