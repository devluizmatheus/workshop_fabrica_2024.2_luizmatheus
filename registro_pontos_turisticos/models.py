from django.db import models

'''Criando as Models para a API e DATABASE'''
class RegistrandoPontosTuristicos(models.Model):
    nome = models.CharField('Nome', max_length=255)
    localizacao = models.CharField('Localização', max_length=255)
    descricao = models.CharField('Descrição', max_length=255)
    horarios = models.CharField('Horários', max_length=255)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
  

    def __str__(self):
        return self.nome