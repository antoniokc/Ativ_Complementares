nota1 = int(input("Por favor insira sua primeira nota: "))
nota2 = int(input("Por favor insira sua segunda nota: "))
nota_optativa = int(input("Por favor insira suas terceira nota: "))
media = (nota1 + nota2 + nota_optativa) / 3


if nota_optativa > nota1 or nota2:
    