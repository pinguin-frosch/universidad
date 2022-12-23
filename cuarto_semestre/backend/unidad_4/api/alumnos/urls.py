from django.urls import path
from alumnos import views

urlpatterns = [
    path('', views.lista_alumnos, name='alumnos'),
    path('<int:id>', views.detalle_alumno, name='detalle_alumno'),
]
