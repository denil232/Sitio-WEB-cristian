from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Obra  # <--- IMPORTANTE: Importamos el modelo Obra

# --- Formulario de Registro (El que ya tenías) ---
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        # Solo ponemos username y email. Las contraseñas las maneja UserCreationForm automáticamente.
        fields = ['username', 'email'] 


# --- NUEVO: Formulario para gestionar las Obras (Para Cristian Erre) ---
class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ['titulo', 'descripcion', 'imagen', 'estado']
        
        # Esto es para que se vea bonito con estilos (clases CSS)
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la obra'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción o historia...'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }