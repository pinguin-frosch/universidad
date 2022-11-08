from django.urls import path
from tipos import views

app_name = 'tipos'
urlpatterns = [
    path('', views.listar, name='listar'),
    path('crear', views.crear, name='crear'),
]