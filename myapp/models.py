from django.db import models
from .funciones import only_str,only_int

# Create your models here.
class Organigrama(models.Model):
    codigo_organigrama = models.CharField(max_length=5)
    nombre_organigrama = models.CharField(max_length=20)
    fecha_organigrama = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre_organigrama
    
class Dependencia(models.Model):
    nombre_dependencia = models.CharField(max_length=25)
    codigo_dependencia = models.CharField(max_length=3)
    codigo_jefe = models.CharField(max_length=4)

    def __str__(self):
        return self.nombre_dependencia
    
class Persona(models.Model):
    codigo_persona = models.CharField(max_length=4)
    documento_persona = models.CharField(validators=[only_int],max_length=9)
    apellido_persona = models.CharField(validators=[only_str],max_length=15)
    nombre_persona = models.CharField(validators=[only_str],max_length=15)
    telofono_persona = models.CharField(validators=[only_int],max_length=12)
    direccion = models.CharField(max_length=30)
    dependencia = models.CharField(validators=[only_int],max_length=3)
    salario = models.CharField(max_length=9)
    
    def __str__(self):
        return self.nombre_persona +" - "+ self.apellido_persona