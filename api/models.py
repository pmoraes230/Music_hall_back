# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Cadeiras(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, choices=[('available', 'Disponivel'), ('reserved', 'Reservado')], default='available')  # Field name made lowercase.
    id_setor = models.ForeignKey('Setores', db_column='ID_SETOR', on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.
    row = models.CharField(max_length=2, blank=True)
    column = models.CharField(max_length=3, blank=True)

    class Meta:
        db_table = 'cadeiras'
        
    def __str__(self):
        return f'{self.id_setor.nome} - {self.row}{self.column} ({self.status})'

class Clientes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E_MAIL', max_length=50)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=14)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientes'
        
    def __str__(self):
        return self.nome

class ClientesEvento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_evento = models.ForeignKey('Evento', db_column='ID_EVENTO', on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.
    id_clientes = models.ForeignKey('Clientes', db_column='ID_CLIENTES', on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientes_evento'
        
    def __str__(self):
        return f'Evento: {self.id_evento.nome}, Cliente: {self.id_clientes.nome}'
        
class Evento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50)  # Field name made lowercase.
    capacidade_pessoas = models.FloatField(db_column='CAPACIDADE_PESSOAS')  # Field name made lowercase.
    imagem = models.ImageField(db_column='IMAGEM', upload_to='eventos/', blank=True, null=True)  # Field name made lowercase.
    data_evento = models.DateField(db_column='DATA_EVENTO')  # Field name made lowercase.
    horario = models.TimeField(db_column='HORARIO')  # Field name made lowercase.
    id_usuario = models.ForeignKey('Usuario', db_column='ID_USUARIO', on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'evento'
        
    def __str__(self):
        return self.nome

class Perfil(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=20)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'perfil'

    def __str__(self):
        return self.nome

class Setores(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50)  # Field name made lowercase.
    qtd_cadeira = models.FloatField(db_column='QTD_CADEIRA')  # Field name made lowercase.
    id_evento = models.ForeignKey('Evento', db_column='ID_EVENTO', on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'setores'
        
    def __str__(self):
        return self.nome

class Usuario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50)  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=50)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E_MAIL', max_length=50)  # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=350,  null=False)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=14)  # Field name made lowercase.
    id_perfil = models.ForeignKey('Perfil', db_column='ID_PERFIL', on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self):
        return self.nome