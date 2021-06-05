medida=float(input('uma distancia em metros:  '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A medida de {}m corresponde a {}dm'.format(medida,dm))
print('A medida de {}m corresponde a {}cm'.format(medida,cm))
print('A medida de {}m corresponde a {}mm'.format(medida,mm))
print('A medida de {}m corresponde a {:.2f}dam'.format(medida,dam))
print('A medida de {}m corresponde a {}hm'.format(medida,hm))
print('A medida de {}m corresponde a {}km'.format(medida,km))
