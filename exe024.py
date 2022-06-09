# Digitar um local e como resposta verificar se a palavra Santo fui digitada.

cidade = str(input('Digite a sua cidade de nascimento: ')).strip()
print(cidade[:5].upper() == 'SANTO')