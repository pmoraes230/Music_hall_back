from django.contrib import admin
from . import models

admin.site.register(models.Usuario)
admin.site.register(models.Clientes)
admin.site.register(models.Evento)
admin.site.register(models.Cadeiras)
admin.site.register(models.ClientesEvento)
admin.site.register(models.Setores)
admin.site.register(models.Perfil)