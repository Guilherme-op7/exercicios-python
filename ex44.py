preço = int(input('digite o valor total das compras R$ '))
print('''DIFERENTES FORMAS DE PAGAMENTO
[ 1 ] A VISTA DINHEIRO/CHEQUE
[ 2 ] A VISTA CARTÃO
[ 3 ] 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO''')
OPÇÃO =int(input('qual é a opção de pagamento? '))
if OPÇÃO == 1:
    total = preço - (preço * 10 / 100)
elif OPÇÃO == 2:
    total = preço - (preço * 5 / 100)
elif OPÇÃO == 3:
    total = preço
    parcela = total / 2
    print('sua compra será parcela em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif OPÇÃO == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('qual é o valor da parcela? '))
    parcela = total / totparc
    print('sua compra sera parcela em {}X de R$ {:.2f} com JUROS'.format(totparc , parcela))
else:
    total = 0
    print('OPÇÃO INVALIDA TENTE NOVAMENTE')
print('sua compra de R${:.2f} vai custar R${:.2f} no final '.format(preço , total))
