casa = float(input('qual é o valor da casa: R$'))
salário = float(input('me imforme seu salário: R$'))
anos = int(input('quantos anos de financiamento: R$'))
prestação = casa / (anos * 12)
minímo = salário * 30 / 100
print('para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos),end='')
print(' a prestação será de R$ {:.2f}'.format(prestação))
if prestação <= minímo:
    print('emprestimo comcedido!')
else:
    print('esprestimo NEGADO!')
