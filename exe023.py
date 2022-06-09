# Informado um numero informe seu milhar, centena, dezena e unidade:

numero = int(input('Informe seu numero: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 100
m = numero // 1000 % 1000
print('O numero digitado foi {}'.format(numero))
print('A unidade do numero é: {}'.format(u))
print('A dezena do numero é: {}'.format(d))
print('A centena do numero é: {}'.format(c))
print('0 milhar do numero é: {}'.format(m))