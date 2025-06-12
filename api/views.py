from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from . import models, serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

    def create(self, request, *args, **kwargs):
        self.permission_classes = []  # Permite criação sem autenticação
        return super().create(request, *args, **kwargs)

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
            usuario = models.Usuario.objects.get(login=login)
        except models.Usuario.DoesNotExist:
            return Response(
                {'message': 'Usuário não encontrado.'},
                status=status.HTTP_404_NOT_FOUND
            )

        if check_password(password, usuario.senha):
            token, created = Token.objects.get_or_create(user_id=usuario.id)
            return Response({
                'token': token.key,
                'user_id': usuario.id,
                'message': 'Login realizado com sucesso!'
            }, status=status.HTTP_200_OK)
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
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class SetoresVieSet(viewsets.ModelViewSet):
    queryset = models.Setores.objects.all()
    serializer_class = serializers.SetoresSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(id_evento_id=self.request.data.get('id_evento'))

    @action(detail=True, methods=['get'])
    def cadeiras(self, request, pk=None):
        setor = self.get_object()
        cadeiras = setor.cadeiras_set.all()
        serializer = serializers.CadeirasSerializer(cadeiras, many=True)
        return Response(serializer.data)
    
class CadeiraViewSet(viewsets.ModelViewSet):
    queryset = models.Cadeiras.objects.all()
    serializer_class = serializers.CadeirasSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['post'])
    def reserve(self, request):
        cadeira_ids = request.data.get('cadeira_ids', [])
        cadeiras = models.Cadeiras.objects.filter(id__in=cadeira_ids, status='available')
        
        if len(cadeiras) != len(cadeira_ids):
            return Response({'error': 'Alguns assentos não estão disponíveis.'}, status=status.HTTP_400_BAD_REQUEST)
        
        cadeiras.update(status='reserved')
        return Response({'message': 'Assentos reservados com sucesso!'}, status=status.HTTP_200_OK)
    
class PerfilViewSet(viewsets.ModelViewSet):
    queryset = models.Perfil.objects.all()
    serializer_class = serializers.PerfilSerializer

class ClienteEventoViewSet(viewsets.ModelViewSet):
    queryset = models.ClientesEvento.objects.all()
    serializer_class = serializers.ClientesEventoSerializer