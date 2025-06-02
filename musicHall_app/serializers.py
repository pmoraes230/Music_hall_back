from rest_framework import serializers
from . import models

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = ['id', 'nome', 'e_mail', 'senha', 'perfil', 'cpf', 'login']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = ['id', 'nome', 'e_mail', 'cpf']

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Evento
        fields = ['id', 'nome', 'qtd_publico', 'id_usuario']

class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Setor
        fields = ['id', 'nome', 'qtd_cadeira', 'id_evento']

class CadeiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cadeira
        fields = ['id', 'status', 'id_setor']

class Setor_cadeira_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.SetorCliente
        fields = ['id_setor', 'id_cliente', 'id']