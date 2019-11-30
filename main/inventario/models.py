from django.db import models
from djmoney.models.fields import MoneyField

# Modelo de productos
class Producto(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=70)
    marca = models.CharField(max_length=70)
    descripcion = models.TextField()
    precio = MoneyField(max_digits=8, decimal_places=2, default_currency='MXN')
    stock_minimo = models.IntegerField(blank=True, null=True)
    stock_maximo = models.IntegerField(blank=True, null=True)
    
    #list_display =('nombre', 'precio')

    def guardar(self):
        self.save()

    def __str__(self):
        return self.nombre

class Stock(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=False, null=False)
    stock_actual = models.IntegerField(blank=False, null=False)

    def guardar(self):
        self.save()

    def __str__(self):
        #return self.producto + self.stock_actual
        #return '%s %s' % (self.producto, self.stock_actual)
        return str(self.producto)

