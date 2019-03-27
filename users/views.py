from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, User


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()