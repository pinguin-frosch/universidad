from django.forms import ModelForm, widgets
from .models import Marca


class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'
        widgets = {
            'nombre': widgets.TextInput(
                attrs={'class': 'form-control'}
            )
        }
