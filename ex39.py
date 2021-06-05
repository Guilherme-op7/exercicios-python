from datetime import date

nascimento = int(input('Qual seu ano de nascimento? '))
atual = date.today().year
idade = atual - nascimento
print('quem nasceu em {}, tem {} anos, em {}'.format(nascimento , idade , atual))
if idade == 18:
    print('você tem que se alistar imediatamente!')
elif idade < 18:
     saldo = 18 - idade
     print('ainda faltam {} anos para que você possa se alistar'.format(saldo))
elif idade > 18:
    saldo = idade -18
    print('você já deveria ter se alistado há {} anos'.format(saldo))