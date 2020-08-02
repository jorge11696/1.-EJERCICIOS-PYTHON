#La maquina eligirá un número y debemos adivinarlo.
import random #Improtamos este modulo para que genere un numero aleatorio.

def run ():
    number_found = False
    random_number=random.randint(0,20)
    while not number_found:
        number= int (input ('Introduzca su número aquí: '))
        if number == random_number:
            print ('Enhorabuena, encontraste el numero!')
            number_found=True
        elif number>random_number:
            print ('El numero es mas pequeño')
        else:
            print('El numero es mas grande')

if __name__=='__main__':
    run()
