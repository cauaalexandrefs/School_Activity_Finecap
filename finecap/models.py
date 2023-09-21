from django.db import models
from django.utils import timezone as time_zone
# Create your models here.


class Stands(models.Model):
    localizacao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.localizacao

    
class Reservas(models.Model):
    nome_empresa = models.CharField(max_length=100)
    CNPJ = models.CharField(max_length=11)
    categoria_empresa = models.CharField(max_length=100)
    quitado = models.BooleanField()
    date = models.DateTimeField(default=time_zone.now)
    stand = models.ForeignKey(Stands, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_empresa