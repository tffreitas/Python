#Ler um numero inteiro e dizer se ele é ou não primo.

num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[1;34m', end=' ')
        tot += 1
    else:
        print('\033[1;31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\33[m0 número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('O número {} é PRIMO!'.format(num))
else:
    print('O número {} não é PRIMO!'.format(num))



