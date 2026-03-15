"""
URLs do app livros.
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("cadastro/sucesso/<int:livro_id>/", views.cadastro_sucesso, name="cadastro_sucesso"),
    path("consulta/", views.consulta, name="consulta"),
    path("resultado/", views.resultado, name="resultado"),
    path("listar/", views.listar, name="listar"),
    path("detalhes/<int:livro_id>/", views.detalhes, name="detalhes"),
    path("excluir/<int:livro_id>/", views.confirmar_exclusao, name="confirmar_exclusao"),
    path("sobre/", views.sobre, name="sobre"),
    path("contato/", views.contato, name="contato"),
]

