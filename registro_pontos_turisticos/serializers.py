# api/serializers.py

from rest_framework import serializers
from .models import RegistrandoPontosTuristicos

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrandoPontosTuristicos
        fields = '__all__'

