#'Llave':'Valor'
KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
   }

def cifrar(mensaje):
    mensaje_separado = mensaje.split()
    mensaje_cifrado = []

    for i in mensaje_separado:
        palabra_cifrada = ''
        for letter in i:
            palabra_cifrada += KEYS [letter]
        mensaje_cifrado.append (palabra_cifrada)
    return ' '.join(mensaje_cifrado)


def descifrar(mensaje):
    mensaje_separado= mensaje.split()
    mensaje_descifrado=[]
    for i in mensaje_separado:
        palabra_descifrada=''
        for letter in i:
            for key, value in KEYS.items():
                if value==letter:
                    palabra_descifrada+=key
        mensaje_descifrado.append(palabra_descifrada)
    return ' '.join(mensaje_descifrado)




def run():
    while True:

        comando = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografía. ¿Que desea hacer?

            [c]ifrar mensaje
            [d]escifrar mensaje
            [s]alir
        '''))

        if comando == 'c':
            mensaje= str(input('Introducir mensaje a cifrar: '))
            resultado = cifrar(mensaje)
            print(resultado)



        elif comando == 'd':
            mensaje = str(input('Introducir mensaje a descifrar: '))
            resultado = descifrar (mensaje)
            print (resultado)
        elif comando == 's':
            print('salir')
        else:
            print('¡Comando no encontrado!')



if __name__ == '__main__':
    print('M E N S A J E S  C I F R A D O S')
    run()
