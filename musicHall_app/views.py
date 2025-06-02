from rest_framework import viewsets, permissions
from . import models
from . import serializers

# Create your views here.
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