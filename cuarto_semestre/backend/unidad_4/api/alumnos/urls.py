from django.urls import path
from alumnos import views

urlpatterns = [
    path('', views.lista_alumnos, name='alumnos')
]
