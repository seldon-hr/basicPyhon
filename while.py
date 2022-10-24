def run():
    LIMITE = 1000 #this represents as a const wiht upper letters

    contador = 0
    potencia_2 = 2 ** contador
    while potencia_2 < LIMITE:
        print('2 elevaod a ' + str(contador) + ' es igual a: ' + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2** contador



if __name__ == '__main__':
    run()
