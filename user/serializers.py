from .models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['phone', 'last_login', 'is_admin',
                  'is_staff', 'created_at', 'updated_at']
