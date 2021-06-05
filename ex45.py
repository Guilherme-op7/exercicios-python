from random import randint
lista = ('PEDRA' , 'PAPEL' ,'TESOURA')
comput = randint (0 , 2 )
print('''SUAS OPÇÕES....
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('ESCOLHA SUA JOGADA '))
print('-=-' * 10)
print('O COMPUTADOR ESCOLHEU {}'.format(lista[comput]))
print('JOGADOR ESCOLHEU {}'.format(lista[jogador]))
print('-=-' * 10)
if comput == 0:#computador jogou pedra
    if jogador == 0:
        print('\033[1;31mEMPATOU!')
    elif jogador == 1:
        print('\033[1;31mJOGADOR VENCEU!')
    elif jogador == 2:
        print('\033[1;31mCOMPUTADOR VENCEU!')
    else:
        print('\033[1;31mOpção Inválida')

elif comput == 1: #computador jogou papel
    if jogador == 0:
        print('\033[1;31mCOMPUTADOR VENCEU')
    elif jogador == 1:
        print('\033[1;31mEMPATOU!')
    elif jogador == 2:
        print('\033[1;31mJOGADOR VENCEU')
    else:
        print('\033[1;31mOpção Inválida')
elif comput == 2:#computaador jogou tesoura
    if jogador == 0:
        print('\033[1;31mJOGADOR VENCEU')
    elif jogador == 1:
        print('\033[1;31mCOMPUTADOR VENCEU')
    elif jogador == 2:
        print('\033[1;31mEMAPATOU')
    else:
        print('\033[1;31mOpção Inválida')