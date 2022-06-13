#programa para calcular o valor a ser pago por um produto considerando o seu peso normal e condição de pagamento:
# A vista: Dinheiro ou Cheque: 10% de desconto
# A vista: Cartão: 5% de Desconto.
# Dividido no Cartão em até 2x: Preço normal
# 3x ou mais no cartão: 20% de Juros.

from datetime import date
hj = date.today() #DATA de HOJE

print('='*10, 'LOJAS THIAGO', '='*10) #Outra forma: print('{:=^40}'.format(' LOJAS THIAGO '))
preco = float(input('Informe o valor da compra (R$): '))
print('''FORMAS DE PAGAMENTO
[ 1 ] A VISTA DINHEIRO/CHEQUE:
[ 2 ] A VISTA CARTÃO:
[ 3 ] 2X CARTÃO:
[ 4 ] 3X OU MAIS NO CARTÃO:''')
opcao = int(input('Informe a opção de pagamento:'))

if opcao == 1:
    print('O valor da compra de R$ {:.2f} com esta opção de pagamento passará para R$ {:.2f}'.format(preco, preco - preco*0.1))
elif opcao == 2:
    print('O valor da compra de R$ {:.2f} com esta opção de pagamento passará para R$ {:.2f}'.format(preco, preco - preco * 5/100))
elif opcao == 3:
    print('O valor da compra de R$ {:.2f} com esta opção de pagamento não terá desconto'.format(preco))
elif opcao == 4:
    parc = int(input('Informe em quantas parcelas: '))
    print('O valor da compra de R$ {:.2f} em {} parcelas com esta opção de pagamento passará para R$ {:.2f}'.format(preco, parc, preco + preco *0.2))
else:
    print('\33[1;31;107mOPÇÃO INVÁLIDA!\33[m')
print('{:=^34}'.format(' FIM '))
hj = str(hj)
print('{:=^34}'.format(hj))

