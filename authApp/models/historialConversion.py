from django.db import models
from .moneda import Moneda

class HistorialConversion(models.Model):
    moneda_origen = models.ForeignKey(Moneda, on_delete=models.CASCADE, related_name='conversiones_origen')
    monto_origen = models.DecimalField(max_digits=10, decimal_places=2)
    moneda_destino = models.ForeignKey(Moneda, on_delete=models.CASCADE, related_name='conversiones_destino')
    monto_destino = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_conversion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return f"{self.monto_origen} {self.moneda_origen.codigo} a {self.monto_destino} {self.moneda_destino.codigo} ({self.fecha_conversion})"
