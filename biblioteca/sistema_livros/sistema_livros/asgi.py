"""
Configuração ASGI (padrão do Django).
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistema_livros.settings")

application = get_asgi_application()

