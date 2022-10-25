def calcular_factorial_menos_uno_y_uno_mas_al_final(numero):
    numero-=1
    contador = numero-1
    while contador != 1:
        numero = numero * contador
        contador -= 1
    return numero + 1

def es_primo(numero):
    multiplo = calcular_factorial_menos_uno_y_uno_mas_al_final(numero)
    if multiplo % numero == 0:
        return True
    else: 
        return False

def run():
    numero = int(input('Escribe un número: '))
    if es_primo (numero):
        print('Es primo')
    else:
        print('No es primo')



if __name__ == '__main__':
    run()