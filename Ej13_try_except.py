paises = {
           'colombia' : 46,
           'argentina' : 32,
           'peru' : 21,
           'Chile': 15
}
while True:
    pais = str (input ('Introduce pais: ')).lower() #Da igual que lo escribamos en mayuscula porque lo pasa a min.
    try:
        print ('La población del pais',pais,'es de:',paises[pais],'millones de habitantes')
    except:
        print('No tenemos informacion del pais',pais)
        print('Lo sentimos!')
