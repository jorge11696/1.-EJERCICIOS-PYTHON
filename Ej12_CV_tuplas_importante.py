#Encontrar el primer caracter o letra que no se repita dentro de un string
"""
"abacabad" c       #c es el primer caracter
"abacabaabacaba" _  # todos se repiten
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d  #d es el primer que no se repite
"bcccccccccccccyb" y  #y es el primero que no se repite
"""

def first_not_repeating_char(char_sequence):
    seen_letters = {} #Iniciamos la variable como un diccionario vacío

    for idx, letter in enumerate(char_sequence):
#Iteramos a lo largo de toda la secuencia de caracteres, obteniendo el indice y cada una de las letras dentro de esta secuencia de caracteres.
        if letter not in seen_letters: #Si esa letra la heemos visto en alguna ocasion, y si no la hemos visto:

            seen_letters[letter] = (idx, 1) #Guardamos la letra en el indice para que nos muestre donde vimos esa letra y cuantas veces hemos visto esa letra.
            #Diccionario y llave = Tupla
            #Utilizamos la letra como la llave y como valor una tupla
#En este caso como no hemos visto la letra significa que es la primera vez que la vemos y por eso ponemos un 1.
        else:  #Si ya vimos la letra y la tenemos almacenada (a 1er ejemplo) modificamos la tupla que esta dentro de la llave con esa letra
            seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1) #Obtenemos el primer valor [0] de esa tupla, las tuplas al igual que las listas se acceden a traves de indices, el primer valor es el indice 0, el segundo lo aumentamos mas 1, obteniendo cuantas veces la vimos mas 1

"""
ejemplo abacabad
seen_letters seria un Diccionario: {
'a':indice de la 1a vez que la vimos, cuantas veces la vimos.
'a: 0,4'
'b: 1,2'
'c: 3,1'
Asi sucesivamente

}
"""
    final_letters = []   #Ahora limpiamos ese diccionario y nos quedamos unicamente con las letras que solo vimos una vez.
#Declaramos variable final_letters que almacena una tupla que nos dira que letras vimos solo una vez y en que indice se encuentra.
    for key, value in seen_letters.items(): #Para obtener llaves y valores utilizamos items.1er Valor tenemos la tupla, en el segundo cuantas veces la vimos.
        if value[1] == 1: #Si la letra la vimos 1 vez vamos a meter una nueva tupla dentro de final_letters, y si la vimos mas de una vez la ignoraremos.
            final_letters.append( (key, value[0]) ) #append para agragar a esta lista y metemos dentro una tupla donde metamos la letra y luego el indice en donde se encuentra esta letra.
"""
ejemplo abacabad
[('a',0) , ('d',7)]
2 Listas con letra e indice (no se repiten)
Lista de tuplas que almacena letra e indice donde la vimos por 1a vez
"""
#Vamos a ordenar esta lista con sorted
    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])
#not_repeated_letters que almacena la misma lista pero ordenada con sorted, recibe una lista final_letters y de segundo parametro va a recibir
#una llave,es decir como queremos que la ordene, gracias a lambda que recibe el valor y regresa el segundo valor
    if not_repeated_letters: #Si not_repeated_letters tiene algo regresamos el primer valor de la lista que es una tupla, obteniendo la letra
        return not_repeated_letters[0][0]
    else:
        return '_' #No encontramos nada, lista vacia, regresamos _



if __name__ == '__main__':
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: ',result)
