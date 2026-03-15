from django.contrib import admin

from .models import Livro


# Registrando o model no admin do Django (bem simples)
admin.site.register(Livro)

