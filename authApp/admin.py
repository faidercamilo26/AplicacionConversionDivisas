from django.contrib import admin
from .models.moneda import Moneda
from .models.tipoCambio import TipoCambio
from .models.historialConversion import HistorialConversion

admin.site.register(Moneda)
admin.site.register(TipoCambio)
admin.site.register(HistorialConversion)
