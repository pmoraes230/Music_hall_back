from django.db import models

class Perfil(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=20)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'perfil'
        
    def __str__(self):
        return self.nome
    
        
class Usuario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50)  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=50)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E_MAIL', max_length=50)  # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=350)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=14)  # Field name made lowercase.
    id_perfil = models.ForeignKey(Perfil, db_column='ID_PERFIL', on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self):
        return self.nome

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

class Evento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50)  # Field name made lowercase.
    capacidade_pessoas = models.FloatField(db_column='CAPACIDADE_PESSOAS')  # Field name made lowercase.
    imagem = models.CharField(db_column='IMAGEM', max_length=100)  # Field name made lowercase.
    data_evento = models.DateField(db_column='DATA_EVENTO')  # Field name made lowercase.
    horario = models.TimeField(db_column='HORARIO')  # Field name made lowercase.
    id_usuario = models.ForeignKey(Usuario, db_column='ID_USUARIO', on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'evento'
        
    def __str__(self):
        return self.nome

class ClientesEvento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    id_evento = models.ForeignKey(Evento, db_column='ID_EVENTO', on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.
    id_clientes = models.ForeignKey(Clientes, db_column='ID_CLIENTES', on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientes_evento'
        
    def __str__(self):
        return f'{self.id_evento.nome} - {self.id_clientes.nome}'


class Setores(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50)  # Field name made lowercase.
    qtd_cadeira = models.FloatField(db_column='QTD_CADEIRA')  # Field name made lowercase.
    id_evento = models.ForeignKey(Evento, db_column='ID_EVENTO', on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'setores'
        
    def __str__(self):
        return self.nome

class Cadeiras(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10)  # Field name made lowercase.
    id_setor = models.ForeignKey(Setores, db_column='ID_SETOR', on_delete=models.CASCADE, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cadeiras'
        
    def __str__(self):
        return self.status