from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FilmDataSerializer
from .models import FilmData


class FilmViewSet(viewsets.ModelViewSet):
    queryset = FilmData.objects.all()
    serializer_class = FilmDataSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = FilmData.objects.filter(type="action")
    serializer_class = FilmDataSerializer
