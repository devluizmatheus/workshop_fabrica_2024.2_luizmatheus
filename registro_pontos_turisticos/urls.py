from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import RegistroViews
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register(r'registro', RegistroViews)

urlpatterns = [
    
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)