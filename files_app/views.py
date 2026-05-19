from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *
from .models import *
from .filters import *

# Create your views here.
class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class FilePublicViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "head", "options"]
    serializer_class = FilePublicSerializer
    queryset = File.objects.filter(is_active=True).order_by("-approved_at")

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = FilePublicFilter
    search_fields = ['name']
    ordering_fields = ['name','approved_at']
