from django.db import models
from django.utils import timezone

# Create your models here.
class Venta(models.Model):
    fecha_venta = models.DateTimeField(
            default=timezone.now)
    stock_maximo = models.IntegerField(blank=True, null=True)

    def guardar(self):
        self.fecha_venta = timezone.now()
        self.save()

    def __str__(self):
        return self.fecha_venta

# # # class Fichero(models.Model):
# # #     # file will be uploaded to MEDIA_ROOT/uploads
# # #     nombre = models.CharField(max_length=70)
# # #     autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
# # #     fichero = models.FileField(upload_to='uploads/')

# # #     def guardar(self):
# # #         self.save()

# # #     def __str__(self):
# # #         return self.nombre