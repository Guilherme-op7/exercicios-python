velocidade = float(input('qual é a velocidade atual do veiculo? '))
if velocidade >80:
    print('multado você ultrapassou o limite de velocidade de 80km/h')
    multa=(velocidade-80) *7
    print('você deve pagar uma multa de {:.2f}!'.format(multa))
print('tenha um bom dia e dirija com cuidado!')
