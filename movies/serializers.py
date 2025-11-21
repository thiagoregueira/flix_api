from rest_framework import serializers
from django.db.models import Avg

from movies.models import Movie
from genres.models import Genre
from actors.models import Actor
from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer


# Serializer para operações manuais (se necessário)
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=500)
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    release_date = serializers.DateField()
    actors = serializers.PrimaryKeyRelatedField(many=True, queryset=Actor.objects.all())
    resume = serializers.CharField(allow_blank=True, required=False)


class MovieListDetailSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        return 'Filme sem avaliações'


class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        return 'Filme sem avaliações'

    # Alternativa sem usar aggregate
    # def get_rate(self, obj):
    # reviews = obj.reviews.all()
    # if reviews:
    #     total_stars = sum(review.stars for review in reviews)
    #     rate = total_stars / reviews.count()
    #     return round(rate, 1)
    # return 'Filme sem avaliações'

    def validate_release_date(self, value):
        if value.year < 1895:
            raise serializers.ValidationError('O ano de lançamento deve ser 1895 ou posterior.')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('O resumo não pode exceder 500 caracteres.')
        return value
