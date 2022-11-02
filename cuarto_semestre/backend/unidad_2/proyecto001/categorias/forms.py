from django.forms import ModelForm, widgets
from categorias.models import Categoria

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre': widgets.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }