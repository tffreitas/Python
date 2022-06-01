# Calcular area de uma parede e a quantidade de tinta.

h = float(input('Qual a altura da parede? '))
l = float(input('Qual a largura da parede? '))
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e a sua área é de {:.3f}m².'.format(h, l, h*l))
print('Para pintar sua parede, você precisará de {:.3f}l de tinta'.format(l*h/2))

