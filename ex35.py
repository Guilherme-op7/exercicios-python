print('-=-' *25)
print('analisando triangulos....')
print('-=-' *25)
a = float(input('primeiro segmento: '))
b = float(input('segundo segmento: '))
c = float(input('terceiro segmento: '))
if a < b + c and b < c + a and c < b + a:
    print('os segmentos acima podem formar um triangulo! ')
else:
    print('os segmento acima não podem formar um triangulo! ')
