def busqueda (numeros,numero_encontrar,bajo,alto):
    if bajo > alto:
        return False
    mitad = int ((bajo + alto) / 2)

    if numeros[mitad] == (numero_encontrar):
        return True
    elif numeros [mitad] > numero_encontrar:
        return busqueda(numeros, numero_encontrar,bajo, mitad -1)
    else:
        return busqueda (numeros, numero_encontrar,mitad +1, alto)






def run():
    numeros=[4,6,7,9,10,13,15,16,18,19,20,23,25,28,31]
    numero_encontrar=int (input('Introducir numero a encontrar: '))
    resultado = busqueda(numeros,numero_encontrar, 0, len(numeros)-1)
    if resultado is False:
        print('El numero no está en la lista')
    if resultado is True:
        print('El numero si está en la lista')


if __name__ == '__main__':
    run()
