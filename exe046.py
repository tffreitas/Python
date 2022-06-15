#Mostrar na tela uma contagem regressiva indo de 10 até 0 com uma pausa de 1s entre eles.

from time import sleep


for c in range(10, -1, -1):
    print(c)
    sleep(0.8)
print('BUM!!')

