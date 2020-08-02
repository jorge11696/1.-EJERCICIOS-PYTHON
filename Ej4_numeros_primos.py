def num_primo(numero):
    if numero < 2:
        return False
    elif numero == 2:
        return True
    elif numero >2 and numero % 2 ==0:
        return False
    for i in range (3, numero):
        if numero % i == 0:
            return False
    else:
        return True
def run():
    numero= int(input('Introduce tu numero aqui: '))
    result= num_primo(numero)
    if result is False:
        print ('Tu numero no es primo')
    else:
        print ('Tu numero es primo')

if __name__=='__main__':
    run()
