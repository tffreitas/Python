# Digitar o peso de 5 pessoas e informar qual o maior e menor peso informado.

maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Qual peso da {}ª pessoa:(Kg) '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}kg.'.format(maior))
print('O menor peso lido foi {}kg.'.format(menor))

