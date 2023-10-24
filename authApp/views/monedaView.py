from rest_framework import generics
from authApp.models.moneda import Moneda
from authApp.serializers.monedaSerializer import MonedaSerializer

class MonedaListCreateView(generics.ListCreateAPIView):
    queryset = Moneda.objects.all()
    serializer_class = MonedaSerializer

class MonedaRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Moneda.objects.all()
    serializer_class = MonedaSerializer