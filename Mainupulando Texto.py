txt = 'Treinamento em Python'

#FATIAMENTO

print(txt[9]) #exibe: t
print(txt[9:13]) #exibe: to e
print(txt[9:22]) #exibe: to em Python
print(txt[9:22:2]) #exibe: t mPto (Pulando de 2 em 2)
print(txt[:9]) #exibe: Treinamen
print(txt[9::3]) #exibe: tePh (Pulando de 3 em 3)

#ANALISE

len(txt) #Informa o tamanho da string
print(txt.count('o')) #Informa quantas vezes a string 'o' aparece
print(txt.find('ent')) #Encontra o inicio da string 'ent'
'Python' in txt

#TRANSFORMAÇÃO

print(txt.replace('Python', 'SQL')) #Altera a string 'Python' por 'Android'
print(txt.upper()) #Altera toda a string pra letras maiusculas
print(txt.lower()) #Altera toda a string pra letras minusculas
print(txt.capitalize()) #Altera todas as letras para minuscula menos a primeira
print(txt.title()) #Altera o inicio de cada palavra para maiuscula













