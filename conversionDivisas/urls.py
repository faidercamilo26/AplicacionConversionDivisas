from django.contrib import admin
from django.urls import path
from authApp.views.conversionView import ConversionView
from authApp.views.monedaView import MonedaListCreateView, MonedaRetrieveUpdateDeleteView
from authApp.views.tipoCambioView import TipoDeCambioListCreateView, TipoDeCambioRetrieveUpdateDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('convert/', ConversionView.as_view()),
    path('' ,MonedaListCreateView.as_view() ),
    path('actualizarmonedas', MonedaRetrieveUpdateDeleteView.as_view()),
    path('tipocambio',TipoDeCambioListCreateView.as_view() ),
    path('actualizartipocambio',TipoDeCambioRetrieveUpdateDeleteView.as_view() ),
]
