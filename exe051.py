#Ler o primeiro termo e razão de uma PA e informar os dez primeiros termos desta progressão

print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

term = int(input('Informe o termo da PA: '))
rz = int(input('Informe a razão da PA: '))
decimo = term + (10 -1) * rz

for c in range(term, decimo + rz, rz):
    print(c, '->', end=' ')
print('FIM')