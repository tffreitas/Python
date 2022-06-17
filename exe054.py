# Solicitar o ano de nascimento de 7 pessoas

from datetime import date
hj = date.today().year
maior = 0
menor = 0

for c in range(1,8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = hj - ano
    if hj - ano > 18:
        maior += 1
    else:
        menor += 1
print('Foram digitados {} maiores de idade.'.format(maior))
print('Foram digitados {} menores de idade'.format(menor))
