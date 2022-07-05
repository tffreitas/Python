# Criar um programa que digite dois numeros e com eles possa escolher uma opção na tela e que só finaliza ao digitar a opção de encerrar o programa:
from time import sleep

num1 = int(input('Primeiro Valor: '))
num2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] maior
    [ 4 ] Novos números
    [ 5 ] Sair''')
    opcao = int(input('>>>>> Qual sua opção? '))
    if opcao == 1:
        som = num1 + num2
        print('A soma de {} e {} é {}'.format(num1, num2, som))
    elif opcao == 2:
        mul = num1 * num2
        print('A multiplicação entre {} e {} é {}'.format(num1, num2, mul))
    elif opcao == 3:
        if num1 > num2:
            print('{} é maior que {}'.format(num1, num2))
        elif num1 == num2:
            print('Os numeros são iguais')
        else:
            print('{} é maior que {}'.format(num2, num1))
    elif opcao == 4:
        print('Informe os numeros novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção Inválida, tente novamente!')
print('Fim do Programa!')



