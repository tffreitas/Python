#PALINDROMO

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('A frase digitada é um PALINDROMO')
else:
    print('A frase digitada não é um PALINDROMO')




