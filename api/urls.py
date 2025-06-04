from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'eventos', views.EventoViewSet)
router.register(r'setores', views.SetoresVieSet)
router.register(r'cadeiras', views.CadeiraViewSet)
router.register(r'perfil', views.PerfilViewSet)
router.register(r'clientes_eventos', views.ClienteEventoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
