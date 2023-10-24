from rest_framework import serializers
from authApp.models.tipoCambio import TipoCambio

class TipoCambioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCambio
        fields = ('moneda_origen', 'moneda_destino', 'tasa_de_cambio', 'fecha_actualizacion')
