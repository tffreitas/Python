# Informar o nome de 4 alunos e com esses 4 alunos informar uma ordem aleatoria entre eles.

import random
a1 = input('Digite o primeiro aluno: ')
a2 = input('Digite o segundo aluno: ')
a3 = input('Digite o terceiro aluno: ')
a4 = input('Digite o quarto aluno: ')
alunos = [a1, a2, a3, a4]
random.shuffle(alunos) # Metodo shuffle "embaralha" a lista fornecida.
print('A ordem de apresentação será: {}'.format(alunos))


