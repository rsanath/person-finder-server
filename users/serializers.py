from rest_framework import serializers
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('full_name',
                  'dob',
                  'email_id',
                  'ph_num',
                  'address',
                  'image',
                  'type',
                  'created_at',
                  'updated_at',
                  'url',
                  'complaints')
