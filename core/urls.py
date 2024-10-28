# urls.py
from django.urls import path
from .views import (
    home, login_view, register, logout_view, agendar_consulta,
    cadastrar_paciente, ver_consultas, editar_consulta, excluir_consulta,buscar_paciente, editar_paciente,excluir_paciente
)

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
    path('agendar_consulta/', agendar_consulta, name='agendar_consulta'),
    path('cadastrar_paciente/', cadastrar_paciente, name='cadastrar_paciente'),
    path('ver_consultas/', ver_consultas, name='ver_consultas'),
    path('editar_consulta/<int:id>/', editar_consulta, name='editar_consulta'),  # Rota para editar consulta
    path('excluir_consulta/<int:id>/', excluir_consulta, name='excluir_consulta'),  # Nova rota para excluir consulta
    path('buscar_paciente/', buscar_paciente, name='buscar_paciente'),
    path('editar_paciente/<int:paciente_id>/', editar_paciente, name='editar_paciente'),
      path('excluir_paciente/<int:paciente_id>/', excluir_paciente, name='excluir_paciente'),
    
]

