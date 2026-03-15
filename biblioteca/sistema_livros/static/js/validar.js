function validarFormulario() {
    // Pegando os valores pelo ID (igual no exemplo do enunciado)
    let titulo = document.getElementById("titulo").value;
    let autor = document.getElementById("autor").value;
    let editora = document.getElementById("editora").value;
    let ano = document.getElementById("ano").value;
    let paginas = document.getElementById("paginas").value;
    let categoria = document.getElementById("categoria").value;
    let isbn = document.getElementById("isbn").value;
    let idioma = document.getElementById("idioma").value;
    let descricao = document.getElementById("descricao").value;
    let cadastradoPor = document.getElementById("cadastrado_por").value;

    // Verificar campos vazios
    if (titulo == "" || autor == "" || editora == "" || ano == "" || paginas == "" || categoria == "" ||
        isbn == "" || idioma == "" || descricao == "" || cadastradoPor == "") {
        alert("Preencha todos os campos!");
        return false;
    }

    // Ano deve ser número
    if (isNaN(ano)) {
        alert("Ano deve ser número!");
        return false;
    }

    // Páginas deve ser maior que 0 (e também ser número)
    if (isNaN(paginas)) {
        alert("Número de páginas deve ser número!");
        return false;
    }

    if (parseInt(paginas) <= 0) {
        alert("Número de páginas deve ser maior que 0!");
        return false;
    }

    return true;
}

