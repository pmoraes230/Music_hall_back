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
    status = models.CharField(db_column='STATUS', max_length=10)  # Field name made lowercase.
    id_setor = models.IntegerField(db_column='ID_SETOR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cadeiras'


class Clientes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E_MAIL', max_length=50)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=14)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientes'


class ClientesEvento(models.Model):
    pk = models.CompositePrimaryKey('ID_EVENTO', 'ID_CLIENTES')
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    id_evento = models.IntegerField(db_column='ID_EVENTO')  # Field name made lowercase.
    id_clientes = models.IntegerField(db_column='ID_CLIENTES')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientes_evento'
        
class Evento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50)  # Field name made lowercase.
    capacidade_pessoas = models.FloatField(db_column='CAPACIDADE_PESSOAS')  # Field name made lowercase.
    imagem = models.CharField(db_column='IMAGEM', max_length=100)  # Field name made lowercase.
    data_evento = models.DateField(db_column='DATA_EVENTO')  # Field name made lowercase.
    horario = models.TimeField(db_column='HORARIO')  # Field name made lowercase.
    id_usuario = models.ForeignKey('Usuario', db_column='ID_USUARIO', on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'evento'

class Perfil(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=20)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'perfil'


class Setores(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50)  # Field name made lowercase.
    qtd_cadeira = models.FloatField(db_column='QTD_CADEIRA')  # Field name made lowercase.
    id_evento = models.IntegerField(db_column='ID_EVENTO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'setores'


class Usuario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50)  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=50)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E_MAIL', max_length=50)  # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=350)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=14)  # Field name made lowercase.
    id_perfil = models.IntegerField(db_column='ID_Perfil', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'
