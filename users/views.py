from django.http import HttpResponse
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework_extensions.mixins import NestedViewSetMixin


from .serializers import UserSerializer, User


class UserViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    STATUS_SUCCESS = 'success'
    STATUS_FAILURE = 'failure'

    def validate_user(self):
        pass

    def make_response(self, status_code, msg, data=None):
        status_msg = self.STATUS_SUCCESS if str(status_code)[0] == '2' else self.STATUS_FAILURE
        res = dict(
            message=msg,
            status=status_msg,
            data=data
        )
        return Response(res, status=status_code)

    @action(detail=False, methods=['POST'])
    def validate_user(self, request, *args, **kwargs):
        data = request.data
        if (
            not data or
            'email' not in data or
            'password' not in data
        ):
            return self.make_response(status.HTTP_400_BAD_REQUEST, 'Validation Error')

        email = data['email']
        password = data['password']

        try:
            user = User.objects.get(email_id=email)
        except User.DoesNotExist:
            return self.make_response(status.HTTP_404_NOT_FOUND, 'No user found with the email {}'.format(email))
            
        if not user.password == password:
            return self.make_response(status.HTTP_401_UNAUTHORIZED, 'Wrong Credentials')

        serializer = UserSerializer(user, context={'request': request})
        return self.make_response(status.HTTP_200_OK, 'Login successful', serializer.data)