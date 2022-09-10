from django.urls import path

from . import views

app_name = 'formulario'
urlpatterns = [
    path('', views.index, name='index'),
    path('saludar/<str:nombre>', views.saludar, name='saludar'),
    path('lista', views.lista, name='lista')
]
