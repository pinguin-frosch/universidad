from django import forms
from personas.models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.widgets.DateInput(attrs={'type': 'date'}),
            'genero': forms.widgets.RadioSelect(choices=[
                ('Masculino', 'Masculino'),
                ('Femenino', 'Femenino'),
                ('No binario', 'No binario'),
            ])
        }