#Script para ler um arquivo .txt e contar quantas palavras existem dentro desse arquivo e mostrar qual palavra se repete mais. 

from collections import Counter

with open('arquivo.txt') as p:
    qtdPalavras = Counter(p.read().split()) #conta quantas vezes as palavras se repetem.

 #printando quantas palavras existem no arquivo
print('Existem ',len(qtdPalavras),'palavras no seu arquivo txt')

#printando qual a palavra que mais se repete e quantas vezes ela aparece.
print('A palavra que mais se repete é ',qtdPalavras.most_common(1),'vezes')
