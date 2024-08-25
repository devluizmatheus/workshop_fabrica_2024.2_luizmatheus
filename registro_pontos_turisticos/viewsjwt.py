from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import RegistrandoPontosTuristicos
from .serializers import RegisterSerializer
'''Criando as views para autenticação do JWT'''
class YourMode(generics.ListCreateAPIView):
    queryset = RegistrandoPontosTuristicos.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]