# Worshop Fábrica de Software 🏭
---
### Criando uma API com o Djando Rest Framework 

Olá Meu nome é Luiz Matheus de Oleveira Leite e irei apresentar o meu projeto para o desafio do Workshop Fábrica de Software e todo o processo que eu fiz estará nesse texto em Markdown ensinando Passo a Passo de como criar essa API

### Sumário
| Indice    | Idade |
|-----|----------------|
| 1°📜     | Requisitos   | 
| 2°🌿     | Criando e Ativando o Ambiente Virtual   | 
| 3°📐   | Primeiros Passos  | 
| 4°⚙️      | Configuração Iniciais| 
| 5°💃|Criando as models|
|6°⬆️|Criando os Serializadores|
|7°🖼️|Criando as ViewSets|
|8°🛜|Criando as Urls|
|9°💻|Até que em fim o teste|

### 1°📜  Requisitos
- Visual Studio Code
- Python 3.12.5
- Django e Django Rest FrameWork
- MySQL instalado 

### 2🌿 ° Criando o Ambiente Virtual
2.1 Crie seu Ambiente Virtual no terminal do vs code
```
python -m venv venv
``` 
2.2 Em seguida ative os Scripts em seu PowerShell como Administrador
```
Set-ExecutionPolicy RemoteSigned
```
2.3 Ative o seu Ambiente virtual no terminal do Vs Code
```
.\venv\Scripts\Activate
```
### 3° 📐 Primeiros Passos
3.1 Instale o Django e o Django Rest Framwork no seu ambiente
```
pip install django djangorestframework pymysql mysqlclient
```
3.2 Crie o Projeto Django
```
django-admin startproject nome_do_projeto .
```
3.3 Crie o Primeiro App do Django
```
django-admin startapp nome_do_app
```
### 4°⚙️ Configruações Iniciais
4.1 Vá até as Settings do projeto e coloque seu app
```
INSTALLED_APPS = [
    'rest_framework',
    'seu_app',
]
}
```
4.2 Vá em data base e coloque a database do MySql
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_pontos_turisticos',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
4.3 Coloque a Lingua em Portugues e o TIMEZONE
```
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Recife'
```
4.4 Adicone os caminhos para as medias
```
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
### 5°💃 Criando os models
5.1 Vá nas models do app e crie
```
from django.db import models

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=255)
    descricao = models.TextField()
    horarios = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='pontos_turisticos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

````
5.2 Registrando as Models na Admin
```
from django.contrib import admin

'''Registrando na Admin'''
from django.contrib import admin
from .models import sua_model

@admin.register(sua_model)
class PontoTuristicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'localizacao', 'descricao', 'horarios')
```
### 6°⬆️ Criando os Serializadores
6.1 Crie um arquivo serializers.py e defina o serializer para o modelo:
```
from rest_framework import serializers
from .models import PontoTuristico

class PontoTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = '__all__'

```
### 7°🖼️ Criando as ViewsSets
7.1 Crie um arquivo ViewSets
```
from rest_framework import viewsets
from .models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(viewsets.ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

```
### 8°🛜 Criando Urls
8.1 Configure as urls
```
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PontoTuristicoViewSet

router = DefaultRouter()
router.register(r'pontos', PontoTuristicoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

```
8.2 Vá para urls do projeto e coloque
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('sua_url.urls')),
]

```
### 9°💻 Até que em fim o Teste
9.1 Crie e aplique as migrações e o super usuario
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

```
9.2 Rode sua Aplicação
```
python manage.py runserver

```

### Considerações Finais!!

Muito obrigado por ter chegado até aqui espero que esse documento tenha ajuda e dou os créditos a os monitores do Workshop por terem me guiado a fazer esse Projeto, muito obrigado!!