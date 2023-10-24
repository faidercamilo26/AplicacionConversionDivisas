from rest_framework import generics
from authApp.models.tipoCambio import TipoCambio
from authApp.serializers.tipoCambioSerializer import TipoCambioSerializer

class TipoDeCambioListCreateView(generics.ListCreateAPIView):
    queryset = TipoCambio.objects.all()
    serializer_class = TipoCambioSerializer

class TipoDeCambioRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoCambio.objects.all()
    serializer_class = TipoCambioSerializer
