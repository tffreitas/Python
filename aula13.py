#estrutura de repetiçao: FOR

'''for c in range(0, 6):
    print(c)

for c in range(6, 0, -1):
    print(c)

for c in range(0, 6, 2):
    print(c)

n = int(input('Digite um numero: '))
for c in range(0, n):
    print(c)

n = int(input('Digite um numero: '))
for c in range(0, n+1):
    print(c)

i = int(input('Digite o primeiro numero: '))
f = int(input('Digite o ultimo numero: '))
p = int(input('Digite o intervalo entre os numeros: '))

for c in range(i, f+1, p):
    print(c)

for c in range(0, 4):
    n = int(input('Digite um valor: '))'''

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s = s + n
print('A soma dos numeros digitados é {}'.format(s))



