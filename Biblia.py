#importando  arquivo auxiliares do professor com o nome aux para ajudar a executar o codigo.
import auxiliares as aux

def calcula_media_palavras_livro(palavras):
    """
    (list) -> (dict)
    Recebe uma lista de palavras e devolve um Dicionário Python onde cada
    chave é uma das palavras passadas como paramêtro e o valor associado é a
    média de ocorrências da palavra nos livros da bíblia.
    """

    #setando um dicionario para biblia 
    biblia = {}

    #Biblia é feita por varios livros então preferi deixar a variavel como Livros para um entendimento melhor do codigo e mais correto.

    livros = 0
    #Procurando nas linhas o final/começo dos novos Livros da biblia.
    for linha in aux.le_biblia():
        if aux.eh_novo_livro(linha):
            livros +=1
    
        for palavra in linha.split():
            if palavra not in biblia:
                biblia[palavra] =1
            else:
                biblia[palavra] +=1
    
    #Criando um dicionario para guardar a quantidade de palavras solicitadas e dividir pela quantidade de livros existentes. 
    dic = {}
    for palavra in palavras:
        if palavra in biblia:
            dic[palavra] = biblia[palavra]/livros
    return dic

#Rodando o script para verificar se é encontrado as palavras.
print(calcula_media_palavras_livro(['Jesus','the','God','light']))
