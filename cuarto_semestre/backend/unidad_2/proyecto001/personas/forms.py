from django import forms
from personas.models import Persona


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'run': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.widgets.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'estado_civil': forms.widgets.Select(
                choices=[
                    ('Solter@', 'Solter@'),
                    ('Casad@', 'Casad@'),
                    ('Divorciad@', 'Divorciad@'),
                    ('Viud@', 'Viud@'),
                ],
                attrs={'class': 'form-control'}),
            'genero': forms.widgets.Select(
                choices=[
                    ('Masculino', 'Masculino'),
                    ('Femenino', 'Femenino'),
                    ('No binario', 'No binario'),
                ],
                attrs={'class': 'form-control'}
            ),
            'direccion': forms.widgets.TextInput(attrs={'class': 'form-control'}),
            'comentario': forms.widgets.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'fono': forms.widgets.TextInput(attrs={'class': 'form-control'}),
        }