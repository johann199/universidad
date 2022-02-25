from cProfile import label
from django import forms

from .models import Curso

class CursoForm(forms.ModelForm):
    
    class Meta:
        model = Curso
        fields = [
            'codigo',
            'nombre',
            'creditos', 
        ]
        labels = {
            'codigo': 'Codigo',
            'nombre':  'Nombre',
            'creditos': 'Creditos' 
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre':  forms.TextInput(attrs={'class': 'form-control'}),
            'creditos': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
    
   
    
    
    
    