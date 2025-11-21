from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from reviews.models import Review
from reviews.serializers import ReviewSerializer
from app.permissions import GlobalPermission


class ReviewListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalPermission]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalPermission]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
