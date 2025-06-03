from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token  # Importa a view para autenticação por token
from . import views

router = routers.DefaultRouter()
router.register(r'usuarios', views.Usuario_list_create)
router.register(r'cliente', views.Cliente_list)
router.register(r'evento', views.Evento_list)
router.register(r'setor', views.Setor_list)
router.register(r'cadeira', views.Cadeira_list)
router.register(r'setor_cadeira', views.Setor_cadeira_list)

urlpatterns = [
    path('', include(router.urls)),
    path('usuarios/login/', views.login_usuario, name='login_usuario'),
    path('get-csrf-token/', views.get_csrf_token, name='get_csrf_token'), # Adiciona o endpoint para obter o token
]