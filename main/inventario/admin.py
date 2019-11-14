from django.contrib import admin
from .models import Producto , Stock 
#from .models import Stock

# Registro de modelos
admin.site.register(Producto)
admin.site.register(Stock)