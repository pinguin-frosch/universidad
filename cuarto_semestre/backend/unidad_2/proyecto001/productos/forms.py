from django.forms import ModelForm, widgets
from productos.models import Producto

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre': widgets.TextInput(
                attrs={'class': 'form-control'}
            ),
            'precio': widgets.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'categoria': widgets.Select(
                attrs={'class': 'form-select'}
            ),
            'marca': widgets.Select(
                attrs={'class': 'form-select'}
            )
        }