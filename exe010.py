#Coversão de Real em Dolar.
# Considerando o dolar $ 5.50

r = float(input('Digite o valor em real que quer fazer a conversão: '))
print('O valor digitado R${:.2f} equivalem a US${:.2f} em dólar'.format(r, (r/5.50)))

