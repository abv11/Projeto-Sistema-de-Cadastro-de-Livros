"""
Views (telas) do sistema.
Tudo bem simples e com comentários, estilo iniciante.
"""

from django.shortcuts import get_object_or_404, redirect, render

from .models import Livro


def home(request):
    return render(request, "home.html")


def cadastro(request):
    """
    Mostra o formulário (GET) e salva o livro (POST).
    """
    erro = ""

    if request.method == "POST":
        # Pegando valores do formulário
        titulo = request.POST.get("titulo", "").strip()
        autor = request.POST.get("autor", "").strip()
        editora = request.POST.get("editora", "").strip()
        ano = request.POST.get("ano", "").strip()
        paginas = request.POST.get("paginas", "").strip()
        categoria = request.POST.get("categoria", "").strip()
        isbn = request.POST.get("isbn", "").strip()
        idioma = request.POST.get("idioma", "").strip()
        descricao = request.POST.get("descricao", "").strip()
        cadastrado_por = request.POST.get("cadastrado_por", "").strip()

        # Validação bem básica no servidor (no front também tem JS)
        if (
            not titulo
            or not autor
            or not editora
            or not ano
            or not paginas
            or not categoria
            or not isbn
            or not idioma
            or not descricao
            or not cadastrado_por
        ):
            erro = "Preencha todos os campos."
        else:
            try:
                ano_int = int(ano)
                paginas_int = int(paginas)
                if paginas_int <= 0:
                    erro = "Número de páginas deve ser maior que 0."
                else:
                    livro = Livro.objects.create(
                        titulo=titulo,
                        autor=autor,
                        editora=editora,
                        ano=ano_int,
                        paginas=paginas_int,
                        categoria=categoria,
                        isbn=isbn,
                        idioma=idioma,
                        descricao=descricao,
                        cadastrado_por=cadastrado_por,
                    )
                    return redirect("cadastro_sucesso", livro_id=livro.id)
            except ValueError:
                erro = "Ano e páginas precisam ser números."

    return render(request, "cadastro.html", {"erro": erro})


def cadastro_sucesso(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    return render(request, "cadastro_sucesso.html", {"livro": livro})


def consulta(request):
    # Só mostra a tela com o campo de pesquisa
    return render(request, "consulta.html")


def resultado(request):
    termo = request.GET.get("q", "").strip()

    livros = []
    mensagem = ""

    if termo == "":
        mensagem = "Digite um nome para pesquisar."
    else:
        livros = Livro.objects.filter(titulo__icontains=termo).order_by("titulo")
        if not livros:
            mensagem = "Nenhum livro encontrado."

    return render(
        request,
        "resultado.html",
        {"livros": livros, "termo": termo, "mensagem": mensagem},
    )


def listar(request):
    livros = Livro.objects.all().order_by("titulo")
    return render(request, "listar.html", {"livros": livros})


def detalhes(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    return render(request, "detalhes.html", {"livro": livro})


def confirmar_exclusao(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    if request.method == "POST":
        # Se confirmou, exclui e volta para a lista
        livro.delete()
        return redirect("listar")

    return render(request, "confirmar_exclusao.html", {"livro": livro})


def sobre(request):
    return render(request, "sobre.html")


def contato(request):
    """
    Formulário simples de contato (não envia email de verdade).
    """
    mensagem = ""
    nome = ""
    email = ""
    texto = ""

    if request.method == "POST":
        nome = request.POST.get("nome", "").strip()
        email = request.POST.get("email", "").strip()
        texto = request.POST.get("mensagem", "").strip()

        if not nome or not email or not texto:
            mensagem = "Preencha todos os campos do contato."
        else:
            # Só "simula" o envio
            mensagem = "Mensagem enviada!"
            nome = ""
            email = ""
            texto = ""

    return render(
        request,
        "contato.html",
        {"mensagem": mensagem, "nome": nome, "email": email, "texto": texto},
    )

