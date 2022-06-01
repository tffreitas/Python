# criar uma tabuada de numeros inteiros.

t = int(input('Digite um número para ver sua tabuada: '))
t1 = t*1
t2 = t*2
t3 = t*3
t4 = t*4
t5 = t*5
t6 = t*6
t7 = t*7
t8 = t*8
t9 = t*9
t10 = t*10
print('-'*12)
print('{} x 1 = {} \n{} x 2 = {} \n{} x 3 = {} \n{} x 4 = {} \n{} x 5 = {} \n{} x 6 = {} \n{} x 7 = {} \n{} x 8 = {} \n{} x 9 = {} \n{} x 10 = {}' .format(t, t1, t, t2, t, t3, t, t4, t, t5, t, t6, t, t7, t, t8, t, t9, t, t10))
print('-'*12)
# Outra forma:

z = int(input('Digite um numero para ver sua tabuada: '))
print('-'*12)
print('{} x {:2} = {}'.format(z, 1, z*1))
print('{} x {:2} = {}'.format(z, 2, z*2))
print('{} x {:2} = {}'.format(z, 3, z*3))
print('{} x {:2} = {}'.format(z, 4, z*4))
print('{} x {:2} = {}'.format(z, 5, z*5))
print('{} x {:2} = {}'.format(z, 6, z*6))
print('{} x {:2} = {}'.format(z, 7, z*7))
print('{} x {:2} = {}'.format(z, 8, z*8))
print('{} x {:2} = {}'.format(z, 9, z*9))
print('{} x {} = {}'.format(z, 10, z*10))
print('-'*12)