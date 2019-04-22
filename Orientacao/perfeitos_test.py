
# Arquivo de testes para as funções do arquivo perfeito.py

#assert serve para verificar se é verdadeiro ou não
import perfeitos as pf

def test_div_2():
    assert pf.lista_divisores(2) == [1]


def test_div_13():
    assert pf.lista_divisores(13) == [1]


def test_div_30():
    assert pf.lista_divisores(30) == [1, 2, 3, 5, 6, 10, 15]


def test_perfeito_5():
    assert not pf.eh_perfeito(5)


def test_perfeito_28():
    assert pf.eh_perfeito(28)


def test_lista_perfeitos_vazia():
    assert pf.lista_perfeitos(5) == []


def test_lista_perfeitos():
    assert pf.lista_perfeitos(28) == [6, 28]


def test_lista_3_perfeitos():
    perf = pf.lista_n_perfeitos(3)
    assert len(perf) == 3


def perf_e_divisores():
    perf = pf.lista_perfeitos_e_divisores(30)
    assert perf == [[6, [1, 2, 3]], [28, [1, 2, 4, 7, 14]]]
