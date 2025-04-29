nota1 = int(input("Por favor insira sua primeira nota: "))
nota2 = int(input("Por favor insira sua segunda nota: "))
nota3 = int(input("Por favor insira suas terceira nota: "))
nota4 = int(input("Por favor insira sua quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media > 7:
    print(f'sua media foi {media} e voce está Aprovado')
elif 5 < media < 7:
    print(f"sua media foi {media} e voce está de recuperação")
else:
    print(f"sua media foi {media} e voce está de reprovação")
