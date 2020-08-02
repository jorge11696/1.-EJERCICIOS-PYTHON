import random


def run ():
    numero = False
    random_numero=random.randint(0,21)

    while not numero == False:
        num=int(input=('Introduce numero'))

        if num > random_numero:
            print('El numero es menor')
            numero=True

        elif num < random_numero:
            print ('El numero es mayor')
        elif num == random_numero:
            print('Enhorabuena, encontraste el numero')

if __name__ == '__main__':
    run()
