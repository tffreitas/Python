#Informar se o ano informado é Bisexto.
# Ano Bisexto ocorrendo a cada quatro anos (exceto anos múltiplos de 100 que não são múltiplos de 400).

ano = int(input('Informe o ano para saber se é bisexto: '))
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print('O ano {} é BISEXTO.'.format(ano))
else:
    print('O ano {} não é BISEXTO.'.format(ano))