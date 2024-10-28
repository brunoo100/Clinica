from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Paciente,  Consulta,Paciente
from .forms import PacienteForm, MedicoForm, ConsultaForm, CustomUserCreationForm, PacienteForm

@login_required  # Garante que somente usuários autenticados possam acessar a home
def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos.'})
    return render(request, 'login.html')


@login_required
def excluir_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('buscar_paciente')  # Redireciona após exclusão
    return render(request, 'excluir_paciente.html', {'paciente': paciente})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login após o logout

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def agendar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_consultas')  # Redireciona após o agendamento
    else:
        form = ConsultaForm()
    return render(request, 'agendar_consulta.html', {'form': form})

@login_required
def cadastrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PacienteForm()
    return render(request, 'cadastrar_paciente.html', {'form': form})

@login_required
def cadastrar_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MedicoForm()
    return render(request, 'cadastrar_medico.html', {'form': form})

@login_required
def ver_consultas(request):
    consultas = Consulta.objects.all()  # Recupera todas as consultas do banco de dados
    return render(request, 'ver_consultas.html', {'consultas': consultas})

@login_required
def editar_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('ver_consultas')
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'editar_consulta.html', {'form': form})

@login_required
def excluir_consulta(request, id):
    consulta = get_object_or_404(Consulta, id=id)
    if request.method == 'POST':
        consulta.delete()
        return redirect('ver_consultas')
    return render(request, 'excluir_consulta.html', {'consulta': consulta})

def confirm_logout(request):
    return render(request, 'confirm_logout.html')  # Página de confirmação

def buscar_paciente(request):
    query = request.GET.get('query', '').strip()
    pacientes = Paciente.objects.filter(nome__icontains=query)
    return render(request, 'buscar_paciente.html', {'pacientes': pacientes})

@login_required
def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('buscar_paciente')  # Redireciona para a página de busca
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'editar_paciente.html', {'form': form, 'paciente': paciente})
