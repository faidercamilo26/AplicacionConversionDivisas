from rest_framework import serializers
from authApp.models.historialConversion import HistorialConversion

class HistorialConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialConversion
        fields = ('moneda_origen', 'monto_origen', 'moneda_destino', 'monto_destino', 'fecha_conversion')
