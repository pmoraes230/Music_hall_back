from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    capacidade_pessoas = models.PositiveIntegerField()
    data_evento = models.DateField()
    horario = models.TimeField()
    descricao = models.TextField(max_length=250, blank=True)
    imagem = models.ImageField(upload_to='eventos/', blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome

class Setores(models.Model):
    id_evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='setores')
    nome = models.CharField(max_length=100)
    qtd_cadeira = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nome} ({self.id_evento})"

class Cadeiras(models.Model):
    id_setor = models.ForeignKey(Setores, on_delete=models.CASCADE, related_name='cadeiras')
    row_assent = models.CharField(max_length=10)
    column_assent = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('reserved', 'Reserved')])

    def __str__(self):
        return f"{self.row_assent}{self.column_assent} ({self.id_setor})"

class Usuario(models.Model):
    login = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.login

class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=191, unique=True)  # Ajustado para 191

    def __str__(self):
        return self.nome

class Perfil(models.Model):
    id_usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class ClientesEvento(models.Model):
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    id_evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_cliente} - {self.id_evento}"