a = int(input('digite o primeiro valor: '))
b = int(input('digite o segundo valor: '))
c = int(input('digite o terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

    maior = a
if b > a  and b > c:
    maior = b
if c > a  and c > b:
    maior = c
print('o menor número digitado foi {}'.format(menor))
print('o maior número digitado foi {}'.format(maior))
