#Calcular a soma entre todos os numeros impares que são multiplos de 3 e que estão no intervalo entre 1 a 500.

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
        print(c, end=' ')
print('\nA soma de todos os {} valores encontrados é {}.'.format(cont, soma))

