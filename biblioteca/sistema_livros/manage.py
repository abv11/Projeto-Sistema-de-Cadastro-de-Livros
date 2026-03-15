#!/usr/bin/env python
"""
Arquivo padrão do Django para rodar comandos do projeto.
Exemplos:
  python manage.py runserver
  python manage.py migrate
"""

import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistema_livros.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django não foi encontrado. Instale com: pip install django\n"
            "Depois tente novamente."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

