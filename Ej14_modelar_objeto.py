
class LamparaDeEscritorio:
# 1.- En el caso de declarar clase no utilizar guin bajo y comenzar con mayusculuas.Keyword para definir clase: class
    _LAMPS =  ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']
# 5.- Generamos una variable clase utilizando ASCII art

    def __init__(self, is_turned_on):
# 2.- lo siguiente para definir dentro de una clase __init__ y recibe un parametro (self)
# 3.- Todos los metodos dentro de las clases deben recibir el parametro self que es la propia instancia
        self._is_turned_on = is_turned_on
# 4.- Definimos las variables que va a tener la instancia, variable privada
    def turn_on (self):
        self._is_turned_on = True
        self._display_image()

    def turn_off(self):
        self._is_turned_on = False
        self._display_image()

# 6.- Definimos variable publica que recibe parametro self (turn_on y turn_off).Con el parametro self conseguimos:
#6.1-Esta es la forma en la que vamos a poder segir accediendo a nuestra instancia y las variables que esta contiene.
#6.2 Lampara nace apagada, si ejecutamos el metodo turn_on se enciende y si ejecutamos el metodo turn_off se apaga.
#7.1 Con cada variable turn_on y turn_off cambiamos estado (encendido y apagado) y mostamos imagen.

    def _display_image (self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])
#7.-Si la lampara esta encendida mostamos 1ª elemento de la lista _LAMPS o el 2º elemento si esta apagada.

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
