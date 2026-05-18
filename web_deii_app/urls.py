from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='api_jwt_token_auth'),
    path('login/verify/', TokenVerifyView.as_view(), name='token_verify'),
]