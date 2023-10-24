from rest_framework import generics
from authApp.models.historialConversion import HistorialConversion
from authApp.serializers.historialConversionSerializer import HistorialConversionSerializer

class HistorialConversionListCreateView(generics.ListCreateAPIView):
    queryset = HistorialConversion.objects.all()
    serializer_class = HistorialConversionSerializer

class HistorialConversionRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistorialConversion.objects.all()
    serializer_class = HistorialConversionSerializer
