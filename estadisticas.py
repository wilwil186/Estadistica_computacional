import random
import math

def media(X):
    return sum(X) / len(X) #El método len() devuelve la longitud de un objeto, ya sea una lista, una cadena, una tupla o un diccionario

def varianza(X):
    mu = media(X)

    acumulador = 0
    for x in X:
        acumulador += (x-mu)**2

    return acumulador / len(X)

def desviacion_estandar(X):
    return math.sqrt(varianza(X))

if __name__ == '__main__':
    X = [random.randint(1, 21) for i in range(20)]
    mu = media(X)
    Var = varianza(X)
    sigma = desviacion_estandar(X)

    print(f'Arreglo x : {X}')
    print(f'Media = {mu}')
    print(f'Varianza = {Var}')
    print(f'Desviación estandar = {sigma}')