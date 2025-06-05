from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from . import models, serializers

# Create your views here.

from django.contrib.auth.hashers import make_password

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

    def create(self, request, *args, **kwargs):
        # Obtém os dados do request
        data = request.data

        # Verifica se os campos obrigatórios estão presentes
        if 'username' not in data or 'password' not in data:
            return Response(
                {'message': 'Username e password são obrigatórios.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Criptografa a senha antes de salvar
        data['password'] = make_password(data['password'])

        # Cria o usuário usando o serializer
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Retorna a resposta com os dados do usuário criado
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
    
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = models.Clientes.objects.all()
    serializer_class = serializers.ClientesSerializer
    
class EventoViewSet(viewsets.ModelViewSet):
    queryset = models.Evento.objects.all()
    serializer_class = serializers.EventoSerializer
    
class SetoresVieSet(viewsets.ModelViewSet):
    queryset = models.Setores.objects.all()
    serializer_class = serializers.SetoresSerializer
    
class CadeiraViewSet(viewsets.ModelViewSet):
    queryset = models.Cadeiras.objects.all()
    serializer_class = serializers.CadeirasSerializer
    
class PerfilViewSet(viewsets.ModelViewSet):
    queryset = models.Perfil.objects.all()
    serializer_class = serializers.PerfilSerializer

class ClienteEventoViewSet(viewsets.ModelViewSet):
    queryset = models.ClientesEvento.objects.all()
    serializer_class = serializers.ClientesEventoSerializer