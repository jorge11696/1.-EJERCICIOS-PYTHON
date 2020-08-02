def palindromo (word):
    reverse_word= word[::-1]
    if reverse_word == word:
        return True

    return False



def run():
    word= input('Introducir palabra: ')
    resultado=palindromo(word)
    if resultado is True:
        print ('Es palindromo')
    else:
        print('No es palindromo')





if __name__ == '__main__':
    run()
