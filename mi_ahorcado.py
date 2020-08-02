import random

IMAGENES= ['''

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

PALABRAS= ['guitarra','raves','cerveza','setas', 'naturaleza','caminar']

def palabra_aleatoria():
    return random.choice(PALABRAS)

def display (palabra_escondida,intentos):
    print (IMAGENES [intentos])
    print('')
    print (palabra_escondida)
    print('####'    '####'    '####'    '####')





def run():

    palabra = palabra_aleatoria ()
    palabra_escondida = ['_'] * len (palabra)
    intentos= 0


    while True:
        display (palabra_escondida,intentos)
        letra_escoger= input ('Introduce tu letra: ')

        indice_letras = []
        for i in range (len (palabra)):
            if palabra [i] == letra_escoger:
                indice_letras.append(i)
        if len (indice_letras) == 0:
            intentos = intentos +1

            if intentos==7:
                display(palabra_escondida,intentos)
                print ('Perdiste, la palabra correcta era',palabra)
                break

        else:
            for i in indice_letras:
                palabra_escondida[i] = letra_escoger

                indice_letras=[]

        try:
            palabra_escondida.index('_')
        except ValueError:
            print ('ENHORABUENA ACERTASTE',palabra)
            break











if __name__ == '__main__':
    print('BIENVENIDOS A AHORCADOS')
    run()
