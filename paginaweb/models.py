from django.db import models


class Tipo_solicitud(models.Model):
    id_tipo_solicitud = models.AutoField(db_column='idTipo_solicitud',primary_key=True)
    tipo_solicitud = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self):
        return str(self.tipo_solicitud)


class Subir(models.Model):
    id_subir = models.AutoField(db_column='idSubir',primary_key=True)
    nombre = models.CharField(max_length= 30)
    id_tipo_solicitud = models.ForeignKey('Tipo_solicitud',on_delete=models.CASCADE, db_column='idTipo_solicitud')
    mensaje = models.TextField(max_length=1000)
    fecha = models.DateField(blank=False, null=False)
    telefono = models.CharField(max_length=9)
    categorias = models.CharField(max_length=50)
    seleccionar = models.CharField(max_length=15)

    def __str__(self):
        return str(self.nombre)+""+str(self.id_tipo_solicitud)
