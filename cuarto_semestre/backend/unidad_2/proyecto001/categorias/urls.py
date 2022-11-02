from django.urls import path
from categorias import views

app_name = 'categorias'
urlpatterns = [
    path('', views.listar, name='listar'),
    path('crear', views.crear, name='crear'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('actulizar/<int:id>', views.actualizar, name='actualizar')
]