from django.contrib import admin
from .models import Paciente, Medico, Consulta

# Customizando a visualização do modelo Paciente no admin
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'telefone', 'endereco')  # Campos exibidos na lista de pacientes
    search_fields = ('nome', 'telefone')  # Permite a busca pelos campos nome e telefone

# Customizando a visualização do modelo Medico no admin
@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'especialidade')  # Campos exibidos na lista de médicos
    search_fields = ('nome', 'crm')  # Permite busca pelo nome do médico e CRM

# Customizando a visualização do modelo Consulta no admin
@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico', 'data', 'hora', 'status')  # Exibe paciente, médico, data, hora e status
    list_filter = ('status', 'data')  # Filtrar por status e data da consulta
    ordering = ('data', 'hora')  # Ordenar por data e hora
