from sys import flags


pesos_colombianos = input('Número de pesos colombianos: ')
pesos_mexicanos = input ('Número de pesos mexicanos: ')


pesos_colombianos = float(pesos_colombianos)
pesos_mexicanos = float(pesos_mexicanos)

valor_dolar_a_colombiano = 3875
valor_dolar_a_mex = 20.12

dolares_colom = pesos_colombianos / valor_dolar_a_colombiano
dolares_colom = round(dolares_colom, 2) #round make to round the number of decimals, and next specifi the number of digits we would like to have after the point.
dolares_colom = str(dolares_colom)
print('Tienes $' + dolares_colom + ' dólares')


dolares_mex = pesos_mexicanos / valor_dolar_a_mex
dolares_mex = round(dolares_mex)
dolares_mex = str(dolares_mex)
print('Tienes estos ' + dolares_mex + ' dólares')