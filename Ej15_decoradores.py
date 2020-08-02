#La idea es generar una funcion protegida frente usuarios no identificados.
def protected(func): #4.-Declaramos una funcion que recibe otra funcion.

    def wrapper (password):#5.-Funcion dentro de una funcion que recibe como parametro la contraseña
        if password == 'platzi':
            return func() #6.-Si es correcta ejecutara nuestra funcion
        else:
            print('La contraseña es incorrecta')

    return wrapper #La funcion protected regresa a la funcion wrapper

@protected # Decoramos nuestra funcion protected(func) al encapsular su comportamiento dentro del wrapper o envoltura. Si recibimos el password correcto la ejecutamos, sino decimos incorrecto.
def protected_func(): #1.-Imprime que es correcta.
    print('Tu constraseña es correcta')



if __name__ == '__main__':
    password = str(input('Ingresa tu constraseña: '))#2.-Entrada ingresar contraseña
    protected_func (password)#3.- Le pasamos a nuestra funcion protegida la contraseña

    #En lugar de @protected:
    #wrapper = protected (protected_func)
    #wrapper(password)
