from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para o painel de administração do Django
    path('', include('core.urls')),    # Inclui as URLs do aplicativo core
]
