def temperatura_media (temp):
    suma_temp = 0
    for i in temp:
        suma_temp += float (i)
        print (suma_temp)
        return suma_temp / len(temp)



def run():
    temp= [20,25,29,35,40]
    resultado= temperatura_media (temp)
    print (resultado)


if __name__ == '__main__':
    run()
