from rest_framework import serializers
from .models import FilmData


class FilmDataSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = FilmData
        fields = ["id", "name", "duration", "rating", "type", "image"]
