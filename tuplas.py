#Ejemplo:
'''
'abacabad' c
'abacabaabacaba' _
'abcdefghijklmnopqrstuvwxyziflskecznslkjfabe' d
'bcccccccccccccyb' y
'''

def first_not_repeating_char(char_sequence):
    my_lista= list(char_sequence) #['a', 'b', 'a', 'c', 'a', 'b', 'a', 'd']
    my_diccionario = {i:my_lista.count(i) for i in my_lista} #{'a': 4, 'b': 2, 'c': 1, 'd': 1}

    caracter_repetido = [] #Iniciamos lista para imprimir luego el caracter repetido.
    for key,value in my_diccionario.items():
        if value == 1:
            caracter_repetido.append ( (key,value) ) #[('c', 1), ('d', 1)] Lista de 2 tuplas, solo muestra las que se repiten 1

    if caracter_repetido:
        return caracter_repetido [0][0] #Regresamos el primer valor de la lista que es una tupla, y el primer valor de la tupla que es la letra 'c' en el ejemplo.
    else:
        return ('-')


char_sequence= str(input('Escribe una secuencia de caracteres: ')) #'abacabad'

resultado = first_not_repeating_char(char_sequence)

if resultado == ('-'):
    print ('Todos tus caracteres se repiten mas de una vez ')
else:
    print ('Tu primer caracter repetido es:', resultado)
