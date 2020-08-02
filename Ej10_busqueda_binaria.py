def binary_search(numbers, number_to_find, low, high):

    if low > high: #Si nuesrto indice bajo mas alto que nuestro indice alto el numero no se encuentra en la lista.
        return False

    mid = int((low + high) / 2) #Indice medio

    if numbers [mid] == number_to_find:
        #Si el numero de la mitad de la lista es el que buscamos.
        return True
    elif numbers[mid] > number_to_find:
        #Si el numero de mitad de la lista es mayor que el que buscamos.
        return binary_search(numbers, number_to_find, low, mid - 1)
        #Buscara desde el indice mas bajo hasta el indice medio menos 1 porque el medio ya esta checkado.
    else:
        #Si el numero de la mitad es menor que el num a buscar.
        return binary_search(numbers, number_to_find, mid + 1, high) # Buscara desde el indice medio +1 hasta el indice alto


if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]

    number_to_find =int (input('Ingresa un número: '))

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1) #Lista de enumeros, numero que queremos encontrar, indice mas bajo y mas alto (len - 1 para no salirnos fuera de nuestro indice)

    if result is True:
        print('El número SI está en la lista.')
    else:
        print('El número NO está en la lista.')
