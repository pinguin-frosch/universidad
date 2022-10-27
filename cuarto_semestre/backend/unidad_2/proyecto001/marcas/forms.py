from django.forms import ModelForm, widgets
from .models import MarcaModel


class MarcaForm(ModelForm):
    class Meta:
        model = MarcaModel
        fields = '__all__'
        widgets = {
            'nombre': widgets.TextInput(
                attrs={'class': 'form-control'}
            )
        }
