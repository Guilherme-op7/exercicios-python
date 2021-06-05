preço = float(input('qual é o valor do produto? R$'))
novo = preço -(preço * 50 /100)
print('o produto que custava R${:.2f}, na promoção com um desconto de 50% vai custar R${:.2f}'.format(preço,novo))
