from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'eventos', views.EventoViewSet)
router.register(r'setores', views.SetoresViewSet)
router.register(r'cadeiras', views.CadeiraViewSet)
router.register(r'perfil', views.PerfilViewSet)
router.register(r'clientes_eventos', views.ClienteEventoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/reservar-cadeira/', views.ReservarCadeirasView.as_view(), name='reservar-cadeiras')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
