produto = int(input('Qual o codigo de origem do produto: '))

match produto:
    case 1:
        print('Produto do Sul')
    case 2:
        print('Produto do Norte')
    case 3:
        print('Produto do Leste')
    case 4:
        print('Produto do Oeste')
    case 5 | 6:
        print('Produto do Nordeste')
    case 7 | 8 | 9:
        print('Produto do Sudeste')
    case 10:
        print('Produto do Centro-oeste')
    case 11:
        print('Produto do Noroeste')
    case _:
        print('Importado')
