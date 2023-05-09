from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

only_str = RegexValidator(r'^[a-zA-Z]*$', 'El campo debe contener solo letras.')

def only_int(value):
    if value.isdigit() == False:
        raise ValidationError("El campo solo acepta numeros")