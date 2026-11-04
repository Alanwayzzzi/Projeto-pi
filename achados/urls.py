from django.urls import path
from . import views

urlpatterns = [
    path("", views.bem_vindo, name="bem_vindo"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("salas/", views.salas, name="salas"),
    path("salas/criar/", views.sala_criar, name="sala_criar"),
    path("salas/entrar/", views.sala_entrar, name="sala_entrar"),
    path("salas/<int:pk>/", views.sala_detalhe, name="sala_detalhe"),
    path("salas/<int:pk>/objetos/adicionar/", views.objeto_adicionar, name="objeto_adicionar"),
    path("objetos/<int:pk>/excluir/", views.objeto_excluir, name="objeto_excluir"),
    path("perfil/", views.perfil, name="perfil"),
]
