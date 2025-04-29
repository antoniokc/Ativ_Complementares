produto = int(input('Qual o codigo para a venda: '))
vl = float(input('Qual o valor do produto: R$'))
vl_dinheiro = vl * 0.10
vl_debito = vl * 0.05
vl_credito = vl * 0.08
vl_cheque = vl * 0.12

match produto:
    case 1:
        print(f'Pagamento como PIX: preço é R${vl}')
    case 2:
        print(f'Pagamento a Vista/Dinheiro: preço é R${vl - vl_dinheiro}')
    case 3:
        print(f'Pagamento como Debito: preço é R${vl + vl_debito}')
    case 4:
        print(f'Pagamento como Credito: preço é R${vl + vl_credito}')
    case 5:
        print(f'Pagamento como Cheque: preço é R${vl + vl_cheque}')
    case _:
        print('modalidade de pagamento invalida')

print('Obrigado pela compra!')
