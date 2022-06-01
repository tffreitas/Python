# Digitar uma distancia em metros e será realizada a conversão pra KM, Hm, Dam, Dm, Cm e Mm.

a = float(input('Digite uma distância em metros: '))
print('A distancia digitada foi {}m. \nO valor de {}m em quilômetros é {}km. \nO valor de {}m em centímetros é {:.0f}cm. \nO valor de {:.0f}m em milimetros é {:.0f}mm.'.format(a, a, (a/1000), a, (a*100), a, (a*1000)))




