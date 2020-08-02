def run():
    counter = 0
    with open ('C:\\Users\\jorge\\Desktop\\PHYTON\\Platzi\\Manejo de datos\\islandia.txt',encoding = 'utf8') as f:
        for line in f:
            counter += line.count(palabra)

        print('La palabra',palabra,'se encuentra',counter,'veces en el texto')


if __name__ == '__main__':
    palabra=str(input ('Escriba la palabra: '))
    run()
