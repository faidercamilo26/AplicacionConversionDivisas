from rest_framework import serializers
from authApp.models.moneda import Moneda


class MonedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moneda
        fields = ('idMoneda', 'nombre', 'codigo', 'simbolo')
