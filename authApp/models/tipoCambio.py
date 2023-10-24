from django.db import models
from .moneda import Moneda
from django.utils import timezone




class TipoCambio(models.Model):
    
    moneda_origen = models.ForeignKey(Moneda, on_delete=models.CASCADE, related_name='tasas_origen')
    moneda_destino = models.ForeignKey(Moneda, on_delete=models.CASCADE, related_name='tasas_destino')
    tasa_de_cambio = models.DecimalField(max_digits=10, decimal_places=4,)
    fecha_actualizacion = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f"{self.moneda_origen.nombre} a {self.moneda_destino.nombre}: {self.tasa_de_cambio}"