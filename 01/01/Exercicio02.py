vendas = int(input('Qual a Quantidade de vendas nesse mês: '))

if vendas >= 100:
    desempenho = 'Excelente'
elif vendas >= 70:
    desempenho = "Bom"
elif vendas >= 30:
    desempenho = 'Regular'
else:
    desempenho = "Insuficiente"

print(f"o desempenho do vendedor foi {desempenho}, ele vendeu {vendas} un")
