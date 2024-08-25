from rest_framework import serializers
from .models import RegistrandoPontosTuristicos

"""Serializando a os Models"""
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrandoPontosTuristicos
        fields = '__all__'

