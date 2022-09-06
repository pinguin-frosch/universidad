from django.urls import path

from . import views

app_name = 'aplicacion'
urlpatterns = [
    path('', views.index, name='index'),
    path('computacion', views.computacion, name='computacion'),
    path('electronica', views.electronica, name='electronica'),
    path('videojuegos', views.videojuegos, name='videojuegos'),
]
