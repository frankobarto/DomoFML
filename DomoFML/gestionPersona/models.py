from django.db import models

# Create your models here.
class Parentesco(models.Model):
    descripcion=models.CharField(max_length=40)

class Tipo_propiedad(models.Model):
    descripcion=models.CharField(max_length=10)

class Tipo_dispositivo(models.Model):
    descripcion_tipo_dispositivo=models.CharField(max_length=10)

class Estado_dispositivo(models.Model):
    descripcion_estado_dispositivo=models.CharField(max_length=10)

class Personas(models.Model):
    nombre_persona=models.CharField(max_length=30)
    correo_persona=models.EmailField()
    nro_celular=models.CharField(max_length=10)
    parentesco=models.ForeignKey(Parentesco, on_delete=models.CASCADE, null=True, default=int(1))
    
    def __str__(self):
        return self.nombre_persona

class Dispositivo(models.Model):
    nombre=models.CharField(max_length=15)
    estado_dispositivo=models.ForeignKey(Estado_dispositivo, on_delete=models.CASCADE, null=True, default=int(1))
    tipo_dispositivo=models.ForeignKey(Tipo_dispositivo, on_delete=models.CASCADE, null=True, default=int(1))

class Propiedad(models.Model):
    direccion=models.CharField(max_length=20)
    tipo_propiedad=models.ForeignKey(Tipo_propiedad, on_delete=models.CASCADE, null=True, default=int(1))


class Evento(models.Model):
    accion=models.BooleanField()
    tipo=models.CharField(max_length=30)

