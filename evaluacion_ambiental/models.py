from django.db import models


# Create your models here.
class Proyectos(models.Model):
    id_table: int = models.IntegerField(null=True)
    nombre: str = models.CharField(max_length=2550)
    tipo: str = models.CharField(max_length=255)
    region: str = models.CharField(max_length=255)
    tipologia: str = models.CharField(max_length=255)
    titular: str = models.CharField(max_length=2550)
    inversion: str = models.CharField(max_length=255)
    fecha_presentacion: str = models.CharField(max_length=255)
    estado: str = models.CharField(max_length=255)

    class Meta:
        unique_together = ('id_table',)
