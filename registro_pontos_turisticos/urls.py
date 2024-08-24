
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import RegistroViews

router = DefaultRouter()
router.register(r'registro', RegistroViews)

urlpatterns = [
    path('', include(router.urls)),
]
