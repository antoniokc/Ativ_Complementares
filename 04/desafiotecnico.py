for i in range(1, 11):
    print(f"\nFuncionario {i}:")
    nomefuncionario = str(input("insira seu nome: "))
    nascimento = int(input("Insira ano de nascimento: "))
    telefone = str(input("Insira o numero de Telefone: "))
    mail = str(input("Insira seu email: "))
    academico = str(input("Insira sua Formação Academica: "))
    exp = str(input("insira sua experiencia profissional: "))
    idade_min = 2025 - nascimento
    if idade_min < 18:
        print("Acesso Negado")
    else:
        print("Acesso Liberado")
