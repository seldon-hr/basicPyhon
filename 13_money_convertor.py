from sys import flags


pesos = input('Número de pesos colombianos: ')
pesos = float(pesos)
valor_dolar = 3875
dolares = pesos / valor_dolar
dolares = round(dolares, 2) #round make to round the number of decimals, and next specifi the number of digits we would like to have after the point.
dolares = str(dolares)
print('Tienes $' + dolares + 'dólares')
