# Aplicar desconto em um valor em Real.

v = float(input('Digite o valor: '))
d = float(input('Digite a porcentagem de desconto: '))
print('O valor {:.2f} com desconto de {:.0f}% terá o novo valor de {:.2f}'.format(v, d, (v-(v*d/100))))

