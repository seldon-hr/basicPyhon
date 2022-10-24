def palindromo(word):
    word = word.replace(' ', '')
    word = word.lower()
    word_opposite = word[::-1]
    if word == word_opposite:
        return True
    else:
        return False

def run():
    word = input('Type a word: ')
    es_palindrom = palindromo(word)
    if es_palindrom == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')


if __name__ == '__main__':
    run()