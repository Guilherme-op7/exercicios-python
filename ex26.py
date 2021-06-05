frase = str(input('digite uma frase ')).upper().strip()
print(' a letra A aparece na frase {} vezes'.format(frase.count('A')))
print(' a letra A apareceu na posição {}'.format(frase.find('A')+1))
print(' a ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))