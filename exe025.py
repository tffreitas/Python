# Verificar se existe a palavra Silva em um nome digitado

nm = str(input('Digite seu nome completo: ')).strip()
nm = nm.upper()
print('Seu nome tem Silva: {}'.format('SILVA' in nm))
