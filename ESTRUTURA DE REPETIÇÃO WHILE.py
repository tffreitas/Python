#Exemplos:

'''n = 1
while n < 10:
    print(n)
    n += 1
print('Fim')'''

'''n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um numero: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} numeros pares e {} numeros ímpares'.format(par, impar))


