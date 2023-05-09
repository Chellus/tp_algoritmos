from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index),
    path('organigramas/',views.organigramas,name="organigramas"),
    path('crear_organigrama/',views.crear_organigrama,name="crear_organigrama"),
    path('crear_dependencia/',views.crear_dependencias,name="crear_dependencia")
]