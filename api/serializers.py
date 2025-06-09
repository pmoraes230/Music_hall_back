from rest_framework import serializers
from . import models

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__'
        
class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clientes
        fields = '__all__'
        
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Evento
        fields = '__all__'

class SetoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Setores
        fields = '__all__'

class CadeirasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cadeiras
        fields = '__all__'
        
class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Perfil
        fields = '__all__'

class ClientesEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClientesEvento
        fields = '__all__'
        depth = 1  # To include related fields in the output
