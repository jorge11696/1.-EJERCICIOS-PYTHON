
import csv #5 Importamos modulo csv de la libreria de python

class Contacto: #Hace de contenedor de las variable name,phone y mail

    def __init__(self,name,phone,mail):
#Para definir el constructor utilizamos __init__
#Los metodos de las clases comienzan con la variable self, y le decimos que esta clase necesita un nombre,tlf, y mail.
        self._name = name
        self._phone = phone
        self._mail = mail
#Inicializamos variables de instancia y las hacemos privadas

class Agenda:
    def __init__(self):  #No recibe ningun parametro
        self._contacts = [] #Lista vacia que recibe los contactos
    def add(self,name,phone,mail): #Para añadir contacto usamos add, un metodo de cada instancia y recibe las variables.
        contacto = Contacto(name,phone,mail) #2 generamos nueva instancia de la clase Contacto y para inicializarla tenemos que pasarle los valores en su constructor.
        self._contacts.append(contacto) #2 agregamos contacto a nuestra lista de contactos.

        self._save() #5 guardamos cada contacto añadido

        print('Nombre: {}, teléfono: {}, mail: {}'.format(name, phone, mail))

    def muestra_todo(self): #2 no recibe ningun parametro
        for contacto in self._contacts:
            self._print_contact(contacto) #2 metodo privado para imprimir contacto

    def _print_contact(self,contacto):
        print('--- * --- * --- * --- * --- * --- * ---')
        print ('Nombre:', contacto._name)
        print ('Teléfono:', contacto._phone)
        print ('Mail:', contacto._mail)
        print('--- * --- * --- * --- * --- * --- * ---')

    def borrar(self,name): #3Iteramos a lo largo de la lista de constactos y si lo encontramos eliminanmos contacto de lista de elementos.
        for idx, contacto in enumerate(self._contacts): #3Necesitamos el indice para borrar elementos, utilizamos enumerate porque tmb nos provee el indice y no solo el elemento
            if contacto._name.lower() == name.lower():#3 lower lo pasa a minusculas
                del self._contacts [idx]#3Borrar con del ese elemento de la lista de contactos a traves de su idx indice
                self._save() #5Guardamos despues de borrar
                break

    def buscar(self,name):
        for contacto in self._contacts: #4Buscamos en la lista de contactos
            if contacto._name.lower() == name.lower():
                self._print_contact(contacto) #Imprimimos contacto con metodo privado
                break
        else: #4 Este else pertenece a for, no a if. Cuando un for loop se ejecuta completamente sin hacer break,entonces ejecutamos else, diciendo que no lo encontramos.
            self._not_found() #4 Ahora falta hacer la def _not_found(self): ....

    def _not_found(self):
        print('--- * --- * --- * --- * --- * --- * ---')
        print('Lo sentimos, contacto no encontrado!')
        print('--- * --- * --- * --- * --- * --- * ---')

    def actualizar(self,name):
        for contacto in self._contacts:
            if contacto._name.lower() == name.lower():
                self.actualizar_contacto(contacto)
                break
        else:
            self._not_found()


    def actualizar_contacto(self,contacto):
        contacto._name = str(input('Añadir nuevo nombre: '))
        contacto._phone = str(input('Añadir nuevo teléfono: '))
        contacto._mail = str(input('Añadir nuevo mail: '))
        print('Contacto actualizado')

    def _save (self): #5 Para guardar contactos en disco duro pc
        with open('Contactos.csv', 'w',) as f: # 5 csv es coma separate values y todo lo separa con comas.
            writer = csv.writer(f) #5 Generamos un writer que vamos a utilizar para escribir y modulo csv y lo importamos arriba del todo
            writer.writerow ( ('name', 'phone', 'Email') ) #5 generamos nuevo writer y definimos la columna (tupla de 3 valores)
            for contacto in self._contacts: #5Por cada contacto en la lista de contactos
                writer.writerow ( (contacto._name, contacto._phone, contacto._mail) ) #5 Vamos a escribir diferentes columnas utilizando el contacto. Tupla de 3 valores

def run():
    contact_book = Agenda() #Generamos nueva instancia de nuestra Agenda, guardamos dentro de la variable concatc_book

    with open ('Contactos.csv', 'r',) as f: #6 Para recrear nuestro softwar cuando lo enchufamos, leeremos ese archivo para no perder contactos guardados.
        reader = csv.reader (f) #6 Generamos reader
        for idx,row in enumerate (reader): #6 Para poder determinar que la primera columna que es la cabecera no queremos utilizarla
            if idx == 0: #6 el primer elemento no lo querimos, seguimos con la iteracion, ya que es la cabecera name,phone,Email y no la queremos
                continue
            if len (row) > 1: #6 por cojones
                contact_book.add(row[0], row[1], row[2]) #6 Si el indice no es 0, utilizamos nuestra clase contact book y le añadimos el contacto, accediendo al primer, segundo y tercer elemento.

    while True:
        command = str(input (''' Qué desea hacer?
        [1] Añadir contacto
        [2] Actualizar contacto
        [3] Buscar contacto
        [4] Eliminar contacto
        [5] Lista de contactos
        [6] Salir
        '''))

        if command == '1':
            name = str(input('Añadir nombre: '))
            phone = str(input('Añadir teléfono: '))
            mail = str(input('Añadir mail: '))

            contact_book.add(name,phone,mail)
        elif command == '2':
            name = str(input('Añadir nombre: '))
            contact_book.actualizar(name)
        elif command == '3':
            name = str(input('Añadir nombre: '))
            contact_book.buscar(name)
        elif command == '4':
            name = str(input('Añadir nombre: '))
            contact_book.borrar(name)
        elif command == '5':
            contact_book.muestra_todo()


        else:
            print ('Gracias, chao!')


if __name__ == '__main__':
    print('AGENDA DE CONTACTOS')
    run()
