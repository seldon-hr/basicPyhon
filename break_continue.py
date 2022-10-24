def run():
    #THIS PRINT ONLY 2, FOR THE DIFERENCE ISN'T EQUAL TO ZERO IT'S MODULE.
    """ for contador in range(1000):
        if contador % 2 != 0:
            continue
        print(contador) """

    #Use with break with numbers    
    """ for i in range(10000):
        print(i)
        if i == 5687:
            break # cut the loop """

    #Break with strings
    texto = input('Type something: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)



if __name__ == '__main__':
    run()