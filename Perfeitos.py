
def divisores(n):
    lista = []
    for i in range(1, n//2+1):
        if n % i == 0:
            lista.append(i)
    return lista


def eh_perfeito(n):
    lista = divisores(n)
    soma = sum(lista)
    if soma == n:
        return True
    else:
        return False


def lista_perfeitos(n):
    lista = []
    for i in range(2, n):
        if eh_perfeito(i):
            lista.append(i)
    return lista


print(lista_perfeitos(10000))
