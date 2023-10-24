from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authApp.models.tipoCambio import  TipoCambio
from authApp.models.moneda import Moneda
from authApp.serializers.monedaSerializer import MonedaSerializer
from authApp.serializers.tipoCambioSerializer import TipoCambioSerializer 

class ConversionView(APIView):
    def post(self, request):
        # Obtener los datos de la solicitud, como la moneda de origen, la cantidad y la moneda de destino
        moneda_origen_id = request.data.get('moneda_origen_id')
        monto_origen = request.data.get('monto_origen')
        moneda_destino_id = request.data.get('moneda_destino_id')

        # Busca las monedas y tasas de cambio correspondientes
        try:
            moneda_origen = Moneda.objects.get(idMoneda=moneda_origen_id)
            moneda_destino = Moneda.objects.get(idMoneda=moneda_destino_id)
            tasa_de_cambio = TipoCambio.objects.get(moneda_origen=moneda_origen, moneda_destino=moneda_destino)
        except (Moneda.DoesNotExist, TipoCambio.DoesNotExist):
            return Response({"error": "Moneda o tasa de cambio no encontrada."}, status=status.HTTP_400_BAD_REQUEST)

        # Realiza la conversión
        monto_destino = monto_origen * tasa_de_cambio.tasa_de_cambio

        return Response({"monto_destino": monto_destino}, status=status.HTTP_200_OK)
