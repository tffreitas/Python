# escrever um programa que faça o computador "pensar" em um numero inteiro de 0 e 5 e
# peça pra o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuario venceu ou perdeu.

from random import randint
pc = randint(0,5) # Faz o pc escolher um número entre 0 e 5.
print('-=-'*19)
print('VOU PENSAR EM UM NÚMERO ENTRE 0 E 5, TENTE ADVINHAR....')
print('-=-'*19)
jg = int(input('Qual número que eu pensei? ')) #jOGADOR TENTA ADVINHAR O NUMERO
if jg == pc:
    print('Parabéns o {} foi o número que eu pensei.'.format(pc))
else:
    print('Você errou, o número que pensei foi {}.'.format(pc))






