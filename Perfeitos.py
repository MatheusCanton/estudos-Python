#lista de perfeitos para usar junto com o codigo perfeitos_test

def lista_divisores(n):
    lista = []
    for i in range(1, n//2+1):
        if n % i == 0:
            lista.append(i)
    return lista


def eh_perfeito(n):
    lista = lista_divisores(n)
    soma = sum(lista)
    if soma == n:
        return True
    else:
        return False


def lista_perfeitos(n):
    lista = []
    for i in range(2, n+1):
        if eh_perfeito(i):
            lista.append(i)
    return lista


def lista_n_perfeitos(n):
    x = 0
    lista = []
    while x < n :
        for i in range(1,x+1):
            if eh_perfeito(i):
                lista.append(i)
                x +=1
    return lista

print(lista_perfeitos(10000))

#instale pytest e verifique se o codigo está correto.
