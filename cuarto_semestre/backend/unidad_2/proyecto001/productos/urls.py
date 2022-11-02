from django.urls import path
from productos import views

app_name = 'productos'
urlpatterns = [
    path('', views.listar, name='listar'),
    path('crear/', views.crear, name='crear'),
    path('actualizar/<int:id>', views.actualizar, name='actualizar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar')
]
