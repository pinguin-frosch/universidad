from django.urls import path

from . import views

app_name = 'clientes'
urlpatterns = [
    path('', views.planes, name='planes'),
    path('lista', views.lista, name='lista')
]