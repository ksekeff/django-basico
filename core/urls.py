from .views import index, contato, produto
from django.urls import path
from django.conf.urls import handler404, handler500
from core import views


urlpatterns = [
    path('', index, name='index'), # Esse paramentro name é usando nos arquivos .html
    path('contato', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto'),
]

handler404 = views.error404
handler500 = views.error500