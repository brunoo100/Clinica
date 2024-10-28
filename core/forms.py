from django import forms
from .models import Paciente, Medico, Consulta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome',  'idade', 'telefone', 'endereco']

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = [ 'nome', 'crm', 'especialidade']

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente', 'medico', 'data', 'hora', 'status']  # Usar data e hora
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        required=True,  # Se necessário, você pode tornar o campo obrigatório
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nome de usuário',
        })
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # Remove o help_text padrão no campo 'username'
        self.fields['username'].help_text = None