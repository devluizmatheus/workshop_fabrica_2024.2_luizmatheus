from rest_framework import viewsets
from .models import RegistrandoPontosTuristicos
from .serializers import RegisterSerializer

"""Criando views para o CRUD"""
class RegistroViews(viewsets.ModelViewSet):
    queryset = RegistrandoPontosTuristicos.objects.all()
    serializer_class = RegisterSerializer

    