from sys import flags

def conversor(tipo_pesos, valor_dolar):
    pesos = input('Número de pesos ' + tipo_pesos + ': ')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) #round make to round the number of decimals, and next specifi the number of digits we would like to have after the point.
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')


menu = """
    Welcome to the coin convertor 😎

1 - Colombian Peso
2 - Argetian Peso
3 - Mexican Peos    

Elige una opción: """

opcion = input(menu)

if opcion == '1':
    conversor('colombianos', 3875)

elif opcion == '2':
    conversor('argentinos', 65)

elif opcion == '3':
    conversor('colombianos', 20)

else:
    print("Insert a valid option, please.")


# pesos_colombianos = input('Número de pesos colombianos: ')
# pesos_mexicanos = input ('Número de pesos mexicanos: ')


# pesos_colombianos = float(pesos_colombianos)
# pesos_mexicanos = float(pesos_mexicanos)

# valor_dolar_a_colombiano = 3875
# valor_dolar_a_mex = 20.12

# dolares_colom = pesos_colombianos / valor_dolar_a_colombiano
# dolares_colom = round(dolares_colom, 2) #round make to round the number of decimals, and next specifi the number of digits we would like to have after the point.
# dolares_colom = str(dolares_colom)
# print('Tienes $' + dolares_colom + ' dólares')


# dolares_mex = pesos_mexicanos / valor_dolar_a_mex
# dolares_mex = round(dolares_mex)
# dolares_mex = str(dolares_mex)
# print('Tienes estos ' + dolares_mex + ' dólares')