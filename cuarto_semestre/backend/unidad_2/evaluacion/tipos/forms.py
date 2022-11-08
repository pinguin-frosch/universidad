from django.forms import ModelForm, widgets
from tipos.models import Tipo


class TipoFormulario(ModelForm):
    class Meta:
        model = Tipo
        fields = '__all__'
        widgets = {
            'nombre': widgets.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
