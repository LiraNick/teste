from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_estabelecimento/', views.cadastro_estabelecimento, name='cadastro_estabelecimento'),
    path('cadastro_mesas/', views.cadastro_mesas, name='cadastro_mesas'),
    path('cadastro_garcon/', views.cadastro_garcon, name='cadastro_garcon'),
    path('cadastro_menu/', views.cadastro_menu, name='cadastro_menu'),
    path('controle_comandas/<int:mesa_id>/', views.controle_comandas, name='controle_comandas'),
    path('calculo_mesa/<int:comanda_id>/', views.calculo_mesa, name='calculo_mesa'),
]