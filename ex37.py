num = int(input('digite um número decimal: '))
print('''escolha uma base para converter
[1]CONVERTER PARA BINARIO
[2]CONVERTER PARA OCTAL
[3]CONVERTER PARA HEXADECIMAL''')
opção = int(input('suas opções:'))
if opção == 1:
    print('{} convertido para BINARIO tem o resultado de {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL tem o resultado de {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL tem o resultado de {}'.format(num, hex(num)[2:]))
else:
    print('opção invalida tente novamente')
