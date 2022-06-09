# Contar quantas vezes aparece a letra a e as posições dela em uma frase.

frase = str(input('Digite sua frase: ')).strip().upper()
print('Sua frase tem {} letras A'.format(frase.count('A')))
print('A primeira letra A esta na posição {}'.format(frase.find('A')+1))
print('A ultima letra A esta na posição {}'.format(frase.rfind('A')+1))



