#Solicitar Nome, Idade e Sexo de 4 pessoas e informar a media de idade do grupo.
# A pessoal mais velha e sua idade e seu nome,
# e a quantidade de pessoas com menos de 20 anos.

smidade = 0
mdidade = 0
maioridade = 0
menoridade = 0
for c in range(1, 5):
    print('-'*5, '{}ª PESSOA'.format(c), '-'*5)
    nome =str(input('Nome: '))
    idade = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: '))
    smidade += idade
    mdidade = smidade/4
    if sex == M and c == 1:
        maioridade = idade
        menoridade = idade


print('A média de idade do grupo é {}.'.format(mdidade))


