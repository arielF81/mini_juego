
#Ejercicio Generar Un Rango Con Una Función
def rango(desde, hasta, intervalo):
    numeros = []
    while desde < hasta:
        numeros.append(desde)
        desde += intervalo
    return numeros
lista = rango(1, 10, 2)
print(lista) 