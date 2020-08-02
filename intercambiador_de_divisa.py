#Intercambiador de € a $
def conversor(Euros):
    E= float (Euros)
    Conversión= E * 1.08
    return Conversión
Euros = input('Introducir cantidad de Euros: ')
Conversión= conversor(Euros)
print(Conversión)
