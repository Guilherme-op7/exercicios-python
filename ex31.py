distancia = float(input('qual e a distancia da sua viagem? '))
print('você esta preste a começar uma viagem de {} km'.format(distancia))
if distancia <= 200:
    preço = distancia *0.50
else:
    preço = distancia *0.45
    print('e o preço de sua passagem será de R${:.2f}'.format(preço))
