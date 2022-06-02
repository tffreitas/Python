# dado uma lista de 4 alunos, escolher aleatoriamente 1 da lista.

import random #Função para "randomizar" elementos.
a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Dite o nome do quarto aluno: ')

lista = [a, b, c, d]
escolhido = random.choice(lista) # Metodo choice da Biblioteca radom escolhe um valor na lista.
print('O aluno escolhido foi: {}'.format(escolhido))
