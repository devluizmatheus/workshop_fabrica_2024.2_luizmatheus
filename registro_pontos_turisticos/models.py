from django.db import models

# Create your models here.
class RegistrandoPontosTuristicos(models.Model):
    nome = models.CharField('Nome', max_length=255)
    localizacao = models.CharField('Localização', max_length=255)
    descricao = models.CharField('Descrição', max_length=255)
    horarios = models.CharField('Horários', max_length=255)

    def __str__(self):
        return self.nome