for i in range(1, 11):
    print(f"\nEstudante: {i}:")
    nota1 = float(input("Insira a primeira nota: "))
    nota2 = float(input("Insira a segunda nota: "))
    nota3 = float(input("Insira a terceira nota: "))
    nota4 = float(input("Insira a quarta nota: "))
    media = nota1 + nota2 + nota3 + nota4 / 4
    if media > 7:
        print(f"Aprovado, sua media foi {media}")
    elif media == 5 | 6 | 7:
        print(f"Em Recuperação, sua media foi {media}")
    else:
        print(f"Reprovado, sua media foi {media}")
