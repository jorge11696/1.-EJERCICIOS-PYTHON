def palindrome(word):
    reversed_word = word[::-1]
    if reversed_word == word:
        return True
    return False
if __name__ == '__main__':
    word=str (input ('Introducir palabra: '))
    result=palindrome(word)
    if result is True:
        print('Es palindromo:',word)
    else:
        print('No es palindromo:',word)
