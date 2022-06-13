#Jogar Jokenpô com o Computador:


print ('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
opc = int(input('Escolha sua opção:'))

from random import choice

list = ['PEDRA', 'PAPEL', 'TESOURA']
pc = choice(list)

from time import sleep

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')

print('=#'*27)
if opc == 0 and pc == 'PEDRA':
    print('Você escolheu a PEDRA e o Computador escolheu PEDRA.')
    print('Houve um EMPATE')
elif opc == 0 and pc == 'PAPEL':
    print('Você escolheu a PEDRA e o Computador escolheu PAPEL.')
    print('O Computador VENCEU!')
elif opc == 0 and pc == 'TESOURA':
    print('Você escolheu a PEDRA e o Computador escolheu TESOURA.')
    print('Você VENCEU!')
elif opc == 1 and pc == 'PEDRA':
    print('Você escolheu a PAPEL e o Computador escolheu PEDRA.')
    print('Você VENCEU!')
elif opc == 1 and pc == 'PAPEL':
    print('Você escolheu a PAPEL e o Computador escolheu PAPEL.')
    print('Houve um EMPATE')
elif opc == 1 and pc == 'TESOURA':
    print('Você escolheu a PAPEL e o Computador escolheu TESOURA.')
    print('O Computador VENCEU!')
elif opc == 2 and pc == 'PEDRA':
    print('Você escolheu a TESOURA e o Computador escolheu PEDRA.')
    print('O Computador VENCEU!')
elif opc == 2 and pc == 'PAPEL':
    print('Você escolheu a TESOURA e o Computador escolheu PAPEL.')
    print('Você VENCEU!')
elif opc == 2 and pc == 'TESOURA':
    print('Você escolheu a TESOURA e o Computador escolheu TESOURA.')
    print('Houve um EMPATE')
else:
    print('\33[1;31;107mSua opção não existe!\33[m')
print('=#'*27)

