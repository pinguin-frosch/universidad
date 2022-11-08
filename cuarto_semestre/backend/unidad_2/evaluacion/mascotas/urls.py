from django.urls import path
from mascotas import views

app_name = 'mascotas'
urlpatterns = [
    path('', views.listar, name='listar'),
    path('crear', views.crear, name='crear'),
    path('actualizar/<int:id>', views.actualizar, name='actualizar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
]
