from random import randint
computador = randint(0,10)
print('-==-' * 22 )
print('vou pensar em um número entre 0 e 10 tente adivinhar......')
print('-==-' * 22 )
jogador =int(input('em que número eu pensei? '))
if jogador==computador:
    print('Parabéns você conseguiu me vencer!')
else:
    print('Te ganhei pensei no número {} não no número {} não foi dessa vez!'.format(computador , jogador))