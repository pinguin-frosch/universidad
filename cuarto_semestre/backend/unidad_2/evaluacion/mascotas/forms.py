from django.forms import ModelForm, widgets
from mascotas.models import Mascota


class MascotaFormulario(ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'
        widgets = {
            'nombre': widgets.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tipo': widgets.Select(
                attrs={
                    'class': 'form-select'
                }
            )
        }
