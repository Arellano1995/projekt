from django.db import models
from django.utils import timezone

# Create your models here.
class Fichero(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fichero = models.FileField(upload_to='uploads/')

    def guardar(self):
        self.save()

    def __str__(self):
        return str(self.fichero) 