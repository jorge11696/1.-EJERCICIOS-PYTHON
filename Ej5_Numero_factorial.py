#El numero factorial  5!= 5 x 4 x 3 x 2 x 1 = 120

def numero_factorial(numero):
    if numero == 0:
        return 1
    return numero * numero_factorial (numero - 1)



try:
    numero=int(input ('Intoduce numero: '))
except:
    print('Por favor,introduce un numero')
    quit()
resultado=numero_factorial(numero)
print(resultado)
