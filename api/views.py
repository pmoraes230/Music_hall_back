from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from . import models, serializers
from rest_framework.permissions import AllowAny  # Importar AllowAny

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer
    permission_classes = [AllowAny]  # Permitir acesso sem autenticação

    def create(self, request, *args, **kwargs):
        self.permission_classes = [AllowAny]  # Já estava público, mantido para clareza
        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
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
            return Response(  # Corrigido: Adicionado "return"
                {'message': 'Senha incorreta.'},
                status=status.HTTP_401_UNAUTHORIZED
            )

class ReservarCadeirasView(APIView):
    permission_classes = [AllowAny]  # Removida obrigatoriedade de autenticação

    def post(self, request):
        event_id = request.data.get('event_id')
        seats = request.data.get('seats', [])

        try:
            for seat in seats:
                cadeira = models.Cadeiras.objects.get(id=seat['seat_id'], id_setor__id=seat['setor_id'])
                if cadeira.status == 'reserved':
                    return Response(
                        {'error': f'Cadeira {cadeira.row_assent}{cadeira.column_assent} já está ocupada.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                cadeira.status = 'reserved'
                cadeira.save()
            return Response({'message': 'Cadeiras reservadas com sucesso'}, status=status.HTTP_200_OK)
        except models.Cadeiras.DoesNotExist:
            return Response({'error': 'Cadeira ou setor inválido.'}, status=status.HTTP_400_BAD_REQUEST)

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = models.Clientes.objects.all()
    serializer_class = serializers.ClientesSerializer
    permission_classes = [AllowAny]  # Permitir acesso sem autenticação

class EventoViewSet(viewsets.ModelViewSet):
    queryset = models.Evento.objects.all()
    serializer_class = serializers.EventoSerializer
    permission_classes = [AllowAny]  # Removida obrigatoriedade de autenticação

    def create(self, request, *args, **kwargs):
        # Definir id_usuario como None ou um usuário padrão se não fornecido
        if not request.data.get('id_usuario'):
            # Exemplo: Usar um usuário padrão (ID 1) ou None
            request.data._mutable = True
            request.data['id_usuario'] = None  # Ou um ID de usuário padrão
            request.data._mutable = False
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class SetoresViewSet(viewsets.ModelViewSet):
    queryset = models.Setores.objects.all()
    serializer_class = serializers.SetoresSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()

    @action(detail=True, methods=['get'])
    def cadeiras(self, request, pk=None):
        setor = self.get_object()
        cadeiras = setor.cadeiras_set.all()
        serializer = serializers.CadeirasSerializer(cadeiras, many=True)
        return Response(serializer.data)

class CadeiraViewSet(viewsets.ModelViewSet):
    queryset = models.Cadeiras.objects.all()
    serializer_class = serializers.CadeirasSerializer
    permission_classes = [AllowAny]  # Removida obrigatoriedade de autenticação

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
    permission_classes = [AllowAny]  # Permitir acesso sem autenticação

class ClienteEventoViewSet(viewsets.ModelViewSet):
    queryset = models.ClientesEvento.objects.all()
    serializer_class = serializers.ClientesEventoSerializer
    permission_classes = [AllowAny]  # Permitir acesso sem autenticação