from django.contrib import admin

'''Registrando na Admin'''
from django.contrib import admin
from .models import RegistrandoPontosTuristicos

@admin.register(RegistrandoPontosTuristicos)
class PontoTuristicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'localizacao', 'descricao', 'horarios')
