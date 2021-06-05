from datetime import date
atual = date.today().year
nascimento = int(input('qual é data do seu nascimento: '))
idade = atual - nascimento
print('o atleta tem {} anos.'.format(idade))
if idade <=9:
    print('CLASSIFICAÇÃO PARA O ATLETA, MIRIM')
elif idade <=14:
    print('CLASSIFICAÇÃO PARA O ATLETA, INFANTIL')
elif idade <=25:
    print('CLASSIFICAÇÃO PARA O ATLETA, JUNIOR')
else:
    print('CLASSIFICAÇÃO PARA O ATLETA, MASTER!')
