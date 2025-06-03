from rest_framework.authtoken.models import Token
from django.middleware.csrf import get_token
from rest_framework import viewsets, permissions
from . import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def get_csrf_token(request):
    token = get_token(request)
    return Response({'csrfToken': token})

@api_view(['POST'])
def login_usuario(request):
    username = request.data.get('username')
    password = request.data.get('password')

    try:
        # Busca o usuário pelo login
        user = models.Usuario.objects.get(login=username)

        # Compara a senha fornecida com a armazenada no banco de dados
        if user.senha == password:
            return Response({"message": "Login bem-sucedido!", "user_id": user.id})
        else:
            return Response({"error": "Credenciais inválidas!"}, status=403)
    except models.Usuario.DoesNotExist:
        return Response({"error": "Usuário não encontrado!"}, status=404)

class Usuario_list_create(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class Cliente_list(viewsets.ModelViewSet):
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer

class Evento_list(viewsets.ModelViewSet):
    queryset = models.Evento.objects.all()
    serializer_class = serializers.EventoSerializer

class Setor_list(viewsets.ModelViewSet):
    queryset = models.Setor.objects.all()
    serializer_class = serializers.SetorSerializer

class Cadeira_list(viewsets.ModelViewSet):
    queryset = models.Cadeira.objects.all()
    serializer_class = serializers.CadeiraSerializer

class Setor_cadeira_list(viewsets.ModelViewSet):
    queryset = models.SetorCliente.objects.all()
    serializer_class = serializers.Setor_cadeira_Serializer