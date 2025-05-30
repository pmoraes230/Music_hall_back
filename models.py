from django.db import models

class Usuario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nome = models.CharField(db_column='NOME', max_length=50, blank=True, null=True)
    e_mail = models.CharField(db_column='E_MAIL', max_length=50, blank=True, null=True)
    senha = models.CharField(db_column='SENHA', max_length=260, blank=True, null=True)
    perfil = models.CharField(db_column='PERFIL', max_length=13)
    cpf = models.CharField(db_column='CPF', max_length=14)
    login = models.CharField(db_column='LOGIN', max_length=50)

    class Meta:
        db_table = 'usuario'
        managed = False

class Cliente(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nome = models.CharField(db_column='NOME', max_length=50)
    e_mail = models.CharField(db_column='E_MAIL', max_length=50)
    cpf = models.CharField(db_column='CPF', max_length=14)

    class Meta:
        db_table = 'cliente'
        managed = False


class Evento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nome = models.CharField(db_column='NOME', max_length=50)
    qtd_publico = models.FloatField(db_column='QTD_PUBLICO')
    id_usuario = models.ForeignKey(Usuario, db_column='ID_USUARIO', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'evento'
        managed = False


class Setor(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nome = models.CharField(db_column='NOME', max_length=50)
    qtd_cadeira = models.FloatField(db_column='QTD_CADEIRA')
    id_evento = models.ForeignKey(Evento, db_column='ID_EVENTO', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'setor'
        managed = False

class Cadeira(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    status = models.CharField(db_column='STATUS', max_length=9)
    id_setor = models.ForeignKey(Setor, db_column='ID_SETOR', on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        db_table = 'cadeira'
        managed = False


class SetorCliente(models.Model):
    id_setor = models.ForeignKey(Setor, db_column='ID_SETOR', on_delete=models.CASCADE, blank=True, null=True)
    id_cliente = models.ForeignKey(Cliente, db_column='ID_CLIENTE', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'setor_cliente'
        managed = False