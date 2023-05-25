from django.db import models
# Create your models here.

class Empresas(models.Model):
    empresa = models.CharField(max_length=40)
    status = models.BooleanField(default=True)


class Empresas_afiliacao(models.Model):
    cnpj = models.BigIntegerField()
    afiliacao = models.CharField(max_length=40)
    status = models.BooleanField(default=True)
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE) 
