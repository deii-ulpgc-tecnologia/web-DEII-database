from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *
from .models import *

# Create your views here.
class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class FilePublicViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "head", "options"]
    queryset = File.objects.all()
    serializer_class = FilePublicSerializer