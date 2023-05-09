from django import forms
from .funciones import only_int, only_str

class crearNuevoOrganigrama(forms.Form):
    codigo_organigrama = forms.CharField(label="Codigo del organigrama",max_length=5,required=True)
    nombre_organigrama = forms.CharField(label="Nombre del organigrama",widget=forms.Textarea)
    
class crearNuevaDependencia(forms.Form):
    codigo_dependencia = forms.CharField(label="Ingresa el codigo de la dependencia",max_length=3)
    nombre_dependencia = forms.CharField(label="Ingresa el nombre de la dependencia",max_length=25)
    codigo_jefe = forms.CharField(label="Ingresa el codigo del jefe",max_length=4)

class Persona(forms.Form):
    codigo_persona = forms.CharField(max_length=4)
    documento_persona = forms.CharField(validators=[only_int],max_length=9)
    apellido_persona = forms.CharField(validators=[only_str],max_length=15)
    nombre_persona = forms.CharField(validators=[only_str],max_length=15)
    telofono_persona = forms.CharField(validators=[only_int],max_length=12)
    direccion = forms.CharField(max_length=30)
    dependencia = forms.CharField(validators=[only_int],max_length=3)
    salario = forms.CharField(max_length=9)