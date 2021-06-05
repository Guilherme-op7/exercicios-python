peso = float(input('digite seu peso kg: '))
altura = float(input('digite sua altura: '))
imc = peso / (altura ** 2 )
print('o imc dessa pessoa e de {:.1f}.'.format(imc))
if imc <=18.5:
    print('você esta abaixo do peso normal')
elif 18.5 <= imc < 25:
    print('você esta no peso normal PARABÉNS!')
elif 25 <= imc < 30:
    print('você esta em sobrepeso')
elif 30 <= imc < 40:
    print('você esta em OBESIDADE!')
elif imc >= 40:
    print('você esta em OBESIDADE MÓRBIDA CUIDADO!')
