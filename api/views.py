from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from . import models, serializers

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

    @action(detail=False, methods=['post'], permission_classes=[])
    def login(self, request):
        login = request.data.get('username')
        password = request.data.get('password')

        if not login or not password:
            return Response(
                {'message': 'Login e senha são obrigatórios.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Busca o usuário pelo login
            usuario = models.Usuario.objects.get(login=login)
        except models.Usuario.DoesNotExist:
            return Response(
                {'message': 'Usuário não encontrado.'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Compara a senha diretamente (texto plano, conforme solicitado)
        if usuario.senha == password:
            try:
                # Tenta obter o token existente para o user_id
                token = Token.objects.filter(user_id=usuario.id).first()
                if not token:
                    # Cria um novo token apenas se não existir
                    token = Token.objects.create(user_id=usuario.id)
                    token.key = Token.generate_key()
                    token.save()
                return Response(
                    {'token': token.key, 'message': 'Login realizado com sucesso!'},
                    status=status.HTTP_200_OK
                )
            except Exception as e:
                return Response(
                    {'message': f'Erro ao gerar token: {str(e)}'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            return Response(
                {'message': 'Senha incorreta.'},
                status=status.HTTP_401_UNAUTHORIZED
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