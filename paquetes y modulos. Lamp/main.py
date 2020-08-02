#Guardaremos la lógica.
from lamp import LamparaDeEscritorio
def run():

    lamp = LamparaDeEscritorio(is_turned_on = False)
    while True:
        command = str(input('''
        ¿Que desea hacer?
           [e]ncender
           [a]pagar
           [s]alir
         '''))

        if command == 'e':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            print('programa terminado')
            break


if __name__ == '__main__':
    run()
