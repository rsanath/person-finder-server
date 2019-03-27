from django.http import HttpResponse
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action

from .serializers import UserSerializer, User


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def validate_user(self):
        pass

    @action(detail=False, methods=['POST'])
    def validate_user(self, request, *args, **kwargs):
        data = request.data
        if (
            not data or
            'email' not in data or
            'password' not in data
        ):
            raise ValidationError

        user = User.objects.get(email_id=data['email'])
        serializer = UserSerializer(user, context={'request': request})
        
        return Response(serializer.data, status=status.HTTP_200_OK)