from django.db.models import fields
from rest_framework import serializers
from .models import BaseUser


# serializer class for the user
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ['id', 'name', 'email', 'password']
