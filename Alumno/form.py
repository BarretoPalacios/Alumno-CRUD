from django import forms
from .models import Alumnos

class AlumnosModelForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = '__all__'
        
        