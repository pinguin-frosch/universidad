from django.urls import path

from . import views

app_name = 'personas'
urlpatterns = [
    path('registro', views.registrar, name='registrar'),
    path('', views.listar, name='listar'),
]
