# Programa para perguntar a distancia de uma viagemem Km. Calcule o preço da passagem cobrando R$ 0.50 por km
# para viagem até 200km de distancia e R$ 0.45 acima disso.

vg = float(input('Informe a distância da viagem: '))
if vg<=200:
    print('O valor da viagem é R$ {:.2f}'.format(vg*0.5))
else:
    print('O valor da passagem é R$ {:.2f}'.format(vg*0.45))
