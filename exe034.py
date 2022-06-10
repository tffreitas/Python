#Informado o salario aplique o seguinte aumento: Para salario superior a 1250 calcule 10%.
# Para Ingeriores ou iguais o aumento é de 15%.

sal = float(input('Informe o salario R$ '))

if sal > 1250:
    print('Você terá um aumento no salario para o valor R$ {}.'.format(sal*0.1 + sal))
else:
    print('Você terá um aumento de salario para o valor R$ {}'.format(sal*0.15 + sal))
