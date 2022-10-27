from django.urls import path

from . import views

app_name = 'personas'
urlpatterns = [
    path('', views.index, name='index'),
    path('registro', views.registro, name='registro'),
    path('editar:<str:run>', views.editar_persona, name='editar'),
    path('eliminar:<str:run>', views.eliminar_persona, name='eliminar')
]