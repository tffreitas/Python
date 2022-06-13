#Estruturas condicionais:

'''if:

elif:

else:'''

#exemplo:

nm = str(input('Qual seu nome? ')).capitalize()
if nm == 'Thiago':
    print('Que nome bonito!')
elif nm == 'Deise' or nm == 'Ingrid' or nm == 'Théo':
    print('Seu nome é bem popular no Brasil.')
else:
    print('Seu nome é bem normal.')
print('Tenha um Bom dia, {}!'.format(nm))
