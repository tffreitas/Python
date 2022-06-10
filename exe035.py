# Verificar se dados tres valores de reta, formam um triangulo.

#Condição para formar um triangulo, a soma de duas retas tem que ser maior que a terceira.

r1 = float(input('Informe o valor da primeira reta: '))
r2 = float(input('Informe o valor da segunda reta: '))
r3 = float(input('Informe o valor da terceira reta: '))

tr1 = (r1 + r2)
tr2 = (r1 + r3)
tr3 = (r2 + r3)

if tr1 > r3 and tr2 > r2 and tr3 > r1:
    print('As retas formam um triângulo.')
else:
    print('Essas retas não formam um triângulo.')


