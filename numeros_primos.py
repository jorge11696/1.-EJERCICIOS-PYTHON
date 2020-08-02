def primo(numero):
    if numero < 2:
        return False
    elif numero == 2:
        return True
    elif numero > 2 and numero % 2 == 0:
        return False
    else:
        for i in range (3,numero):
            if numero % i == 0:
                return False

    return True


numero=int (input('Ingresa un número: '))
resultado = primo(numero)
if resultado is True:
    print ('Enhorabuena tu numero SI es primo', numero)
else:
    print('Enhorabuena tu numero NO es primo', numero)
