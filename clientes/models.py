from django.db import models
from django.utils.timezone import now

class Cliente(models.Model):
    nome = models.CharField('nome', max_length=30)
    sobrenome = models.CharField('sobrenome', max_length=30)
    cidade = models.CharField('cidade', max_length=30, blank=True, null=True)
    estado = models.CharField('estado', max_length=30, blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)
    foto = models.ImageField(upload_to='foto_dos_clientes', blank=True, null=True)
    criado_em = models.DateField(default=now, editable=False)

    def __str__(self):
        return f'<Cliente {self.nome} {self.sobrenome}>'
