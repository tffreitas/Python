#Escreve um porgrama que crie um numero inteiro qualquer e peça ao usuario qual a base de conversão:
# - 1 para Binário:
# - 2 para Octal
# - 3 para Hexadecimal

num = int(input('Digite um número inteiro: '))
print('Escolha uma das Bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] conveter para HEXADECIMAL')
opc = int(input('Sua opção: '))

if opc == 1:
    print('O numero inteiro {} em BINÁRIO é {}.'.format(num, bin(num)[2:]))
elif opc == 2:
    print('O numero inteiro {} em OCTAL é {}.'.format(num, oct(num)[2:]))
elif opc == 3:
    print('O numero inteiro {} em HEXADECIMAL é {}.'.format(num, hex(num)[2:]))
else:
    print('\33[1;31mOpção Inválida!\33[m')

