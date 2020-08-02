import random    #importamos aleatorio para que escoga palabras de la lista.

#ASCII ART
#IMAGES en mayúsculas porque es una constante y asi diferenciarla de una variable.
#Una constante no puede ser cambiada, una variable si.
#Los corchetes indican lista.


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

#Defino una constante WORD y una lista de palabras.

WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'
]


def random_word():
    idx = random.randint(0, len(WORDS) - 1) #Creamos un indice de palabras aleatorias, y queremos un numero aleatorio entre 0 y la longitud(len) de nuestra lista de palabras -1 para no salirnos fuera del indice.
    return WORDS[idx] #Nos regresará una palabra al azar de nuestra lista de palabras.


def display_board(hidden_word, tries):
    print(IMAGES[tries]) #Imprimir nuestras imagenes con el indice(espacio)
    print('') #Espacio
    print(hidden_word) # Para ver los intentos
    print('--- * --- * --- * --- * --- * --- ')


def run():
    word = random_word()
    hidden_word = ['-'] * len(word) #Para que muestre tantos huecos escondidos como letras tenga la palabra aleatoria.
    tries = 0 #Guardara cuantas veces hemos tenido errores y acceder a nuestra lista de imagenes.

    while True:
#Para que muestre el tablero, la imagen del ahorcado.
        display_board(hidden_word, tries)
        current_letter = str(input('Escoge una letra: ')) #La letra se almacena en la variable current_letter.

        letter_indexes = [] #Nueva lista para checkar si la letra que puso el usuario es correcta se almacena para usarla despues.
        for idx in range (len(word)): #Iteramos a lo largo de la longitud de nuestra palabra
            if word [idx] == current_letter: #Si la letra de la palabra aleatotia es igual a la que el usuario introdujo:
                letter_indexes.append (idx) #La metemos en nuestro indice utilizando append.
        if len (letter_indexes) == 0: #Si nuestro intento de acertar la letra no fue exitoso:
            tries+=1 #Cada vez que no acertemos suma y muestra la siguiente imagen
            if tries == 7: #Porque son 7 imagenes y pierdes
                display_board (hidden_word, tries)
                print('')
                print('Perdiste! La palabra correcta era: ', word)
                break


        else:
            for idx in letter_indexes:
                hidden_word [idx] = current_letter #Cambiamos '-' por la letra acertada.
            letter_indexes = [] #Volvemos a dejar vacia nusra lista y empezamos otra vez.

        try:
            hidden_word.index('-') #Para que busque si quedan dichos simbolos
        except:
            print('Felicidades, acertaste la palabra',word)
            break




if __name__ == '__main__':
    print('B I E N V E N I D O S  A  A H O R C A D O S')
    run()
