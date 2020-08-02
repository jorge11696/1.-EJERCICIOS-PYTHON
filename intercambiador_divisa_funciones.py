def calcular(Euros):
    tasa= Euros * 1.08
    return tasa


def run():
    Euros=float(input('Introducir Euros: '))
    resultado=calcular(Euros)
    print (resultado)






if __name__=='__main__':
    run()
