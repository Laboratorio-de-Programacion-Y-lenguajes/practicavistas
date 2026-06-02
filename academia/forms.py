from django import forms
from .models import Curso
import datetime


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ["titulo", "instructor", "fecha_inicio", "fecha_fin"]
        widgets = {
            "titulo": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ej: Python Básico"}
            ),
            "instructor": forms.Select(attrs={"class": "form-select"}),
            # Forzamos un input de tipo fecha (calendario nativo del navegador)
            "fecha_inicio": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "fecha_fin": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }

    def clean_titulo(self):
        # 'cleaned_data' es el diccionario con datos limpios que pasaron las reglas básicas
        titulo = self.cleaned_data.get("titulo")

        if len(titulo) < 5:
            # ValidationError interrumpe el guardado y devuelve el error al template
            raise forms.ValidationError(
                "El título del curso debe tener al menos 5 caracteres."
            )

        return titulo

    def clean_fecha_inicio(self):
        fecha_inicio = self.cleaned_data.get("fecha_inicio")

        if fecha_inicio is not None and fecha_inicio < datetime.date.today():
            raise forms.ValidationError("La fecha no puede ser antes que hoy")
        return fecha_inicio

    def clean(self):
        fecha_fin = self.cleaned_data.get("fecha_fin")
        fecha_inicio = self.cleaned_data.get("fecha_inicio")

        if (
            fecha_fin is not None
            and fecha_inicio is not None
            and fecha_fin < fecha_inicio
        ):
            raise forms.ValidationError(
                "La fecha de finalización no puede ser antes que la de inicio"
            )
        return self.cleaned_data
