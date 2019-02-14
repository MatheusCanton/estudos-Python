#banco
accounts = [
    { 
        "login": "matheus",
        "senha": "matheus"
    },
    {
        "login": "greg",
        "senha": "greg"
    },
    {
        "login": "root",
        "senha": "root"
    }
]

maxlogin = 3
loginTentativas = 0
usuarioEncontrado = False

while loginTentativas < maxlogin:
    loginTentativas = loginTentativas + 1
    
    #login senha
    userLogin = input("Informe seu login:")
    password = input("Informe a sua senha:")
    
    #loop em accounts
    for acc in accounts:
        #se login existir
        if acc["login"] + acc["senha"] == userLogin + password:
            print("Usuario logado!")
            loginTentativas = maxlogin
            usuarioEncontrado = True
            break

    if not usuarioEncontrado:
        print("Usuario nao encontrado. Tente novamente.")

            
