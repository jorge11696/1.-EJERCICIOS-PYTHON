#Programa para calcular la media de temps.
def media_temps(temps):
    sum_of_temps= 0
    for temp in temps: #Por cada temperatura dentro de las tempreaturas.
        sum_of_temps += float (temp) #Se la sumamos a la variable de temperatura
    return sum_of_temps/ len(temps) #Parametro len para la cantidad de temperaturas
temps = [21,10,19,20,15,14]
media media_temps(temps)
print('El promedio de tempreraturas es de: ',media)
