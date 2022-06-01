# Realizar aumento de valor informando a porcentagem.

s = float(input('Digite o valor do salário do funcionário:R$ '))
a = float(input('Informe o valor em porcentagem do aumento:R$ '))
print('O salário R${:.2f} com o aumento de {:.0f}% passará para R${:.2f}'.format(s, a, (s+(s*a/100))))

