# Com o valor do angulo em graus, informe o seno, o cosseno e a tangente.
from math import sin, cos, tan, radians #Necessario usar a função radians pra transformar o angulo em radianos.
a = float(input('Digite o ângulo que deseja: '))
c = cos(radians(a))
s = sin(radians(a))
t = tan(radians(a))
print('O seno do angulo {:.0f} é: {:.1f}'.format(a, s))
print('O cosseno do angulo {:.0f} é: {:.1f}'.format(a, c))
print('A tangente do angulo {:.0f} é: {:.1f}'.format(a, t))
