from django.contrib import admin
from django.urls import path, include
from core.views import index, contato

urlpatterns = [
    path('admin/', admin.site.urls), # Nao usar o nome admin por segurança. Usar outro nome
    path('',include('core.urls')),
]
