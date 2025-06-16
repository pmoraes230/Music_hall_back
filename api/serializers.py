from rest_framework import serializers
from . import models
from django.contrib.auth.hashers import make_password

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = ['id', 'nome', 'login', 'senha', 'e_mail', 'cpf', 'id_perfil']
        extra_kwargs = {
            'senha': {'write_only': True, 'required': True},
            'cpf': {'required': True},
            'login': {'required': True},
            'e_mail': {'required': True},
        }

    def validate_cpf(self, value):
        cpf = value.replace('.', '').replace('-', '')
        if not cpf:
            raise serializers.ValidationError("O CPF não pode estar vazio.")
        queryset = models.Usuario.objects.filter(cpf=cpf)
        if self.instance:
            queryset = queryset.exclude(id=self.instance.id)
        if queryset.exists():
            raise serializers.ValidationError("Este CPF já está registrado.")
        return value

    def validate_login(self, value):
        if not value:
            raise serializers.ValidationError("O login não pode estar vazio.")
        queryset = models.Usuario.objects.filter(login=value)
        if self.instance:
            queryset = queryset.exclude(id=self.instance.id)
        if queryset.exists():
            raise serializers.ValidationError("Este login já está registrado.")
        return value

    def validate_e_mail(self, value):
        if not value:
            raise serializers.ValidationError("O e-mail não pode estar vazio.")
        queryset = models.Usuario.objects.filter(e_mail=value)
        if self.instance:
            queryset = queryset.exclude(id=self.instance.id)
        if queryset.exists():
            raise serializers.ValidationError("Este e-mail já está registrado.")
        return value

    def validate_senha(self, value):
        if not value:
            raise serializers.ValidationError("A senha não pode estar vazia.")
        return value

    def create(self, validated_data):
        validated_data['senha'] = make_password(validated_data['senha'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'senha' in validated_data:
            validated_data['senha'] = make_password(validated_data['senha'])
        return super().update(instance, validated_data)

class EventoSerializer(serializers.ModelSerializer):
    setores = serializers.SerializerMethodField()

    class Meta:
        model = models.Evento
        fields = '__all__'

    def validate_capacidade_pessoas(self, value):
        if value <= 0:
            raise serializers.ValidationError("A capacidade de pessoas deve ser maior que zero.")
        return value

    def get_setores(self, obj):
        setores = obj.setores_set.all()
        return SetoresSerializer(setores, many=True).data

class SetoresSerializer(serializers.ModelSerializer):
    id_evento = serializers.PrimaryKeyRelatedField(
        queryset=models.Evento.objects.all(),
        required=True,
        allow_null=False
    )
    cadeiras = serializers.SerializerMethodField()

    class Meta:
        model = models.Setores
        fields = ['id', 'nome', 'qtd_cadeira', 'id_evento', 'cadeiras']

    def validate_qtd_cadeira(self, value):
        if value <= 0:
            raise serializers.ValidationError("A quantidade de cadeiras deve ser maior que zero.")
        return value

    def validate(self, attrs):
        id_evento = attrs.get('id_evento')  # Objeto Evento do PrimaryKeyRelatedField
        qtd_cadeira = attrs.get('qtd_cadeira', 0)

        # Valida a capacidade do evento
        evento = id_evento
        total_cadeiras = sum(setor.qtd_cadeira for setor in evento.setores.all()) + qtd_cadeira
        if total_cadeiras > evento.capacidade_pessoas:
            raise serializers.ValidationError(
                f"A soma de cadeiras ({total_cadeiras}) excede a capacidade do evento ({evento.capacidade_pessoas})."
            )
        return attrs

    def get_cadeiras(self, obj):
        cadeiras = obj.cadeiras_set.all()
        return CadeirasSerializer(cadeiras, many=True).data

class CadeirasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cadeiras
        fields = ['id', 'id_setor', 'status', 'row_assent', 'column_assent']

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clientes
        fields = '__all__'

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Perfil
        fields = '__all__'

class ClientesEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClientesEvento
        fields = '__all__'
        depth = 1