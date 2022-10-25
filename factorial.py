def calcular_factorial(numero):
    contador = numero-1
    while contador != 1:
        numero = numero * contador
        contador -= 1
    return numero


def run():
    numero = int(input('Escribe un número: '))
    print('Factorial: ' + str(calcular_factorial(numero)))



if __name__ == '__main__':
    run()