from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'tag', TagViewSet, basename='tag')
router.register(r'file', FilePublicViewSet, basename='file')
urlpatterns = [
    path('', include(router.urls)),
]