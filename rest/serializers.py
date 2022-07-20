from rest_framework import serializers
from .models import student

class studentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField(max_length=50)
    city = serializers.CharField(max_length=100)