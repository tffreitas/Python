# Digitar um numero e mostra o anterior e sucessor.

a1 = int(input('Digite um número: '))
a2 = a1 - 1
a3 = a1 + 1
print('O numero digitado é {}, Seu Antecessor é {} e seu Sucessor é {} ' .format(a1, a2, a3))

# Outra forma:

a1 = int(input('Digite um número: '))
print('O número digitado é {}, seu Antecessor é {} e seu Sucessor é {}.'.format(a1, a1-1, a1+1))



