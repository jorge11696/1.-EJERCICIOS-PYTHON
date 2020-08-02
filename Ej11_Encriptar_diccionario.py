#Diccionario
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

def cypher(message):  #Funcion encriptar
    words = message.split(' ') #Separamos la frase a encriptar a traves de espacios gracias a split.
    cypher_message = [] #Creamos una lista vacia

    for word in words:
        cypher_word = ''   #Declaramos una variable vacía.
        for letter in word:
            cypher_word += KEYS[letter]
#Por cada letra de la palabra cojemos nuestro cypher_word y construimos nuestro codigo cifrado letra a letra.
#Accedemos a nuestro diccionario KEYS[letter] y almacenamos el codigo encriptado correspondiente a cada letra en nuestro cypher_word.
        cypher_message.append(cypher_word) #Añadimos la palabra cifrada a nuestro mensaje cifrado

    return ' '.join(cypher_message)   #Reconstruimos el mensaje para que por cada espacio junte las letras.
#Resumen:Deconstruimos el mensaje dividiendolo en espacios, las palabras en letras, las letras las utilizamos como
#llaves en nuestro diccionario obteniendo la letra cifrada, reconstruimos el mensaje cifrado.

def decipher(message):   #Funcion descriptar
    words = message.split(' ') #Dividimos el mensaje por espacios.
    decipher_message = []   #Lista vacia

    for word in words:
        decipher_word = ''   #Declaramos string vacia

        for letter in word:

            for key, value in KEYS.items():#OJO Como no podemos acceder al diccionario a traves de su valor
#itineraremos a lo largo de todas las llaves y si encontramos el valor podemos obtener la llave o letra.
#Para obtener tanto las llaves como los valores utilizamos items.
                if value == letter:  #si encontramos el valor
                    decipher_word += key  #Metemos la letra o llave en la variable.

        decipher_message.append(decipher_word)#Añadimos cada palabra dentro del mensaje para montar la frase
#Append mete el valor al final de la lista

    return ' '.join(decipher_message) #Recontruimos la oracion con join.


def run():

    while True:

        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a criptografí­a. ¿Qué deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))

        if command == 'c':
            message = str(input('Escribe tu mensaje: '))
            cypher_message = cypher(message)
            print(cypher_message)

        elif command == 'd':
            message = str(input('Escribe tu mensaje tu cifrado: '))
            decypher_message = decipher(message)
            print(decypher_message)
        elif command == 's':
            print('salir')
        else:
            print('¡Comando no encontrado!')


if __name__ == '__main__':
    print('M E N S A J E S  C I F R A D O S')
    run()
