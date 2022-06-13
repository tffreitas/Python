#VErificar se dados 3 segmentos se eles formam um triangulo.
# Caso formem um triângulo mostrar se o Triangulo é
# Equilatero = todos os lados iguais
# Isoceles = dois lados iguais
# Escalenos = todos os lados diferentes.

a = int(input('Informe o valor do primeiro segmento de reta: '))
b = int(input('Informe o valor do segundo segmento de reta: '))
c = int(input('Informe o valor do terceiro segmento de reta: '))

trgulo = bool((a + b) > c and (a + c) > b and (b + c) > a)

if a == b and a == c: # Outra forma a == b == c
    print('O triangulo é \33[1;32mEQUILÁTERO\33[m!')
elif trgulo == True and a == b or a == c:
    print('O triângulo é \33[1;32mISÓCELES\33[m!')
elif trgulo == True and a != b and a != c: #outra forma a != b != c != a
    print('O triângulo é \33[1;32mESCALENO\33[m!')
else:
    print('Os segmentos de reta informados \33[1;31mNÃO\33[m formam um triângulo.')

