from django.urls import path

from . import views

app_name = 'personas'
urlpatterns = [
    path('', views.registro, name='registro'),
    path('lista', views.lista, name='lista')
]