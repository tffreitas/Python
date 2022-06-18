#Solicitar Nome, Idade e Sexo de 4 pessoas e informar a media de idade do grupo.
# O homem mais velho e sua idade e seu nome,
# e a quantidade de mulheres com menos de 20 anos.

smidade = 0
mdidade = 0
maioridade = 0
nomedovelho = ''
menoridade = 0
smulheres = 0
for c in range(1, 5):
    print('-'*5, '{}ª PESSOA'.format(c), '-'*5)
    nome =str(input('Nome: '))
    idade = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).upper()
    smidade += idade
    mdidade = smidade/4
    if c == 1 and sex == 'M': #OUTRA FORMA: sex in 'Mm' sem a necessidade de .upper() na variavel sex
        maioridade = idade
        nomedovelho = nome
    if sex in 'Mm' and idade > maioridade:
        maioridade = idade
        nomedovelho = nome
    if sex == 'F' and idade < 20:
        smulheres += 1
print('A média de idade do grupo é de {} anos.'.format(mdidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridade, nomedovelho))
print('A quantidade de mulheres com menos de 20 anos é {}.'.format(smulheres))
