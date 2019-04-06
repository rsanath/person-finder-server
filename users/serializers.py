from rest_framework import serializers
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'full_name',
            'dob',
            'sex',
            'email_id',
            'ph_num' ,
            'password',
            'address' ,
            'image_url',
            'type',
            'created_at',
            'updated_at',
            'complaints',
            'url'
        )