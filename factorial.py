def factorial (Numero):
    if Numero == 0:
        return 1
    return Numero * factorial (Numero - 1)


Numero=input('Introduce tu numero aqui: ')
Numero = int (Numero)
multiplicacion = factorial (Numero)
print (multiplicacion)
