# Com a informação de dois catetos encontrar a hipotenusa.

c1 = float(input('Digite o valor do cateto oposto: '))
c2 = float(input('Digite o valor do cateto adjacente: '))
h = (c1**2 + c2**2)**(1/2)
print('Como o valor do cateto oposto é {:.2f} e o cateto adjacente é {:.2f}. O valor da hipotenusa é {:.2f}'.format(c1, c2, h))

