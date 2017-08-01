from django import forms 
import datetime
from .models import Purpose


class PurposeForm(forms.ModelForm):
    fecha_inicio =  forms.DateField(initial=datetime.date.today, label='Inicio')
    fecha_fin =  forms.DateField(initial=datetime.date.today, label='Fin')
    class Meta:
        model = Purpose
        fields = [
            "nombre",
            "fecha_inicio",
            "fecha_fin",
            "meta",
            "descripcion"
        ]