#Solicitar Nome, Idade e Sexo de 4 pessoas e informar a media de idade do grupo.
# A pessoal mais velha e sua idade e seu nome,
# e a quantidade de pessoas com menos de 20 anos.

idade = 0
for c in range(1, 5):
    print('-'*5, '{}ª PESSOA'.format(c), '-'*5)
    nome =str(input('Nome: '))
    idade = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: '))
    idade += 1
print(idade)
