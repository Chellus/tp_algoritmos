from django.contrib import admin
from .models import Persona,Organigrama,Dependencia,Persona

# Register your models here.
admin.site.register(Organigrama)
admin.site.register(Dependencia)
admin.site.register(Persona)
