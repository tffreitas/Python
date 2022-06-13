# Programa para aprovar emprestimo bancario para compra de uma casa.
# O programa vai perguntar o valor da casa, o salario do comprador
# e em quantos anos ele vai pagar. Será calculado
# o valor da prestação mensal sabendo que ela não pode exceder 30% do salario ou então o emprestimo será negado.

valor = float(input('Informe o valor da casa: R$ '))
salario = float(input('Informe o salário do comprador: R$ '))
tempo = int(input('Informe quantos anos deseja financiar: '))

mes = tempo*12 #transforma o tempo em ano digitado em meses.
prest = valor/mes

print('Para financiar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}.'.format(valor, tempo, prest))
if (valor/mes) > salario*0.3:
    print('\33[1;31mFINANCIAMENTO NEGADO!\33[m')
else:
    print('\33[1;32mFINANCIAMENTO APROVADO!\33[m')
