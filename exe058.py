#Criar um programa para o computador pensar em um numero e voce tentar acertar. Caso não acerte continue perguntando até acertar.
from time import sleep
from random import randint

print('Sou seu computador...')
sleep(1)
print('Acabei de pensar em um numero entre 0 e 10')
sleep(1)
pc = randint(0, 10)
print('Será que consegue advinhar qual foi?')
sleep(1)
tentativas = 0
acertou = False
while not acertou:
    num = int(input('Qual seu palpite? '))
    tentativas += 1
    if num == pc:
        acertou = True
    else:
        if num < pc:
            print('Mais.. Tente outra vez.')
        elif num > pc:
            print('Menos... Tente outra vez.')
print('Acertou em {} tentativas. Parabéns!!'.format(tentativas))
