# Criar uma tabuada com um numero diitado pelo usuario:

t = int(input('Digite um número para ver sua tabuada: '))

print('-'*12)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(t, c, t*c))
print('-'*12)