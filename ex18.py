
from math import radians, sin, cos , tan
angulo = float(input('digite o angulo que voce deseja: '))
seno = sin(radians(angulo))
print('o angulo de {} tem o SENO  de {:.2f}'.format(angulo , seno))
cosseno = cos(radians(angulo))
print('o angulo de {} tem o cosseno de {:.2f}'.format(angulo , cosseno))
tangente =tan(radians(angulo))
print(' o angulo de {} tem a TANGENTE  de {:.2f}'.format(angulo , tangente))