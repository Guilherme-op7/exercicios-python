n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 + n2) /2
print('tirando a nota {} e a nota {} a média do aluno é {}'.format(n1 , n2 , m))
if  m >=5 and m < 7:
    print('o aluno está de RECUPERAÇÃO!.')
elif m < 5:
    print('o aluno está REPROVADO!.')
elif m > 7:
    print('o aluno está APROVADO PARABÉNS')
