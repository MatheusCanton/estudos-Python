import re


def le_biblia():
    """
    Devolve um arquivo interável com as linhas da bíblia.
    """
    return open('HolyBible.txt', 'r')


def le_teste():
    """
    Devolve um arquivo interável com as linhas do arquivo
    'ArquivoTeste.txt'.
    """
    return open('ArquivoTeste.txt', 'r')


def eh_novo_livro(linha):
    """
    Devolve True caso a linha passada seja o início de
    um novo livro da Bíblia.
    """
    return bool(re.search(r'^Book\s\d\d', linha))
