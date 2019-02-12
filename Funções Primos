def primo(n):
                #(start/stop/step)
    for i in range(2,n//2+1):
        if n % i == 0:
            return False
    return True

def ListaPrimos(n):

    lista = []
    for i in range(2,n):

        if primo(i):
            lista.append(i)
    return lista

def FatoraEmPrimos(n):
    if  primo(n):
        return [[n,1]]
    lista = []
    for i in ListaPrimos(n//2+1):
        pot = 0
        while n % i == 0:
            pot += 1
            n = n // i
        if pot > 0:
            lista.append([i,pot])
    return lista

#teste
print(FatoraEmPrimos(1024))
