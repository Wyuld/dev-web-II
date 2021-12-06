from django.db import models
from django.db.models.deletion import PROTECT
from django.contrib.auth.models import User

class Empregador(models.Model):
    class Meta:
        verbose_name_plural="Empregadores"
    razaoSocial = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=20)

    def __str__(self):
        return self.razaoSocial

class VagaDeEmprego(models.Model):
    class Meta:
        verbose_name_plural="Vagas de Emprego"
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    empregador = models.ForeignKey(Empregador, on_delete=PROTECT, related_name="empregos")

class Inscricao(models.Model):
    class Meta:
        verbose_name_plural="Inscricoes"
    usuario = models.ForeignKey(User, on_delete=PROTECT, related_name="inscricoes")
    vaga = models.ForeignKey(VagaDeEmprego, on_delete=PROTECT, related_name="inscricoes")