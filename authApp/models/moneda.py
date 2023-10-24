from django.db import models

class Moneda(models.Model):
    
    idMoneda = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=5)
    simbolo = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre