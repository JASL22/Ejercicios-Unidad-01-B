import math

def algoritmo_1(lista):
    product = 0
    for x in lista:
        product = product * x
    return product


def algoritmo_2(lista):
    product = 1
    for x in lista:
        product = product * x
    return product


def algoritmo_3(lista):
    product = 1
    for x in lista:
        if x == 0:
            product = 0
            return product
        product = product * x
    return product

def comparar_algoritmos():
    casos_prueba = [
        [1, 2, 3, 4],      # Sin ceros
        [5, 0, 2],         # Con un cero
        [0, 1, 2, 3],      # Cero al inicio
        [1, 2, 3, 0],      # Cero al final
        [0, 0, 0],         # Todos ceros
        [-1, 2, -3, 4],    # Números negativos
        []                 # Lista vacía
    ]
    
    for i, caso in enumerate(casos_prueba):
        print(f"\nCaso de prueba {i+1}: {caso}")
        print(f"Algoritmo 1: {algoritmo_1(caso)}")
        print(f"Algoritmo 2: {algoritmo_2(caso)}")
        print(f"Algoritmo 3: {algoritmo_3(caso)}")

comparar_algoritmos()
