"""
URLs do projeto.
Aqui a gente inclui as URLs do app "livros".
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("livros.urls")),
]

