#CURSO INTRODUÇÃO ORIENTAÇÃO A OBJETOS ALURA
#CRIANDO CONTA NO BANCO COM SUAS FUNÇÕES BASICA PARA USAR COMO TESTE DO ARQUIVO CONTA.PY
def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo {}".format(conta["saldo"]))