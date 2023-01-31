nivelAcesso = input("Digite o nível de acesso: ").upper()

if nivelAcesso == "ADM" or nivelAcesso == "USR":
    genero = input("Digite o seu gênero: ").upper()
    if nivelAcesso == "ADM":
        if genero == "FEMININO":
            print("Olá, administradora!")
        else:
            print("Olá, administrador!")
    else:
        if genero == "FEMININO":
            print("Olá, usuária!")
        else:
            print("Olá, usuário!")
elif nivelAcesso == "GUEST":
    print("Olá, visitante!")
else:
    print("Olá, desconhecido(a)!")
