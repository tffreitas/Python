#exemplos:

'''for c in range(0, 5):
    print('OI')
print('FIM')

for c in range(0, 5):
    print('OI')
    print('FIM')

for c in range(0,10):
    print(c)

for c in range(0,10):
    print(c+1)'''

produtos = ['coca', 'pepsi', 'guarana', 'sprit', 'fanta']
producao = ['15000', '12000', '13000', '5000', '250']

tamanho = len(produtos)
for i in range(tamanho):
    print('{} unidades produzidas de {}'.format(producao[i], produtos[i]))


