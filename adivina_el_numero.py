import random
#importa una librería para poder hacer operaciones con números aleatorios.

def run():
    numero_aleatorio = random.randint(1, 100) #Aquí la usamos, y para esto, indicamos que nos brinde la opción de un rango de números, y específicamos el rango de números sobre nuestro aleatorio
    numero_elegido = int(input('Elige un número del 1 al 100:'))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un  número más grande.')
        else:
            print('Busca un numero más pequeño')
        numero_elegido = int(input('Elige otro número: '))
    print('Ganaste!')

if __name__ == '__main__':
    run()