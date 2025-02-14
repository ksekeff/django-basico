from .views import index, contato, produto
from django.urls import path


urlpatterns = [
    path('', index, name='index'), # Esse paramentro name é usando nos arquivos .html
    path('contato', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto'),
]